rm(list=ls())
loc="C:/Users/cjacobik/Desktop/Personal/uphex"
setwd(loc)

library(mclust)
library(zoo)

calcSSE=function(d){
  colnames(d)=c("forecast","actual")
  d=d[d[,"forecast"]!=0,]
  d[,"error"]=((d[,"forecast"]-d[,"actual"])/d[,"forecast"])^2
  return(sum(d[,"error"]))
}

dowmodel=function(d,cc){
  d[,"dow"]=unclass(as.POSIXlt(d[,"index"]))$wday+1
  plotted=F
  if(exists("fdf")) rm(list=c("fdf"))
  for(dow in unique(d[,"dow"])){
    dd=d[d[,"dow"]==dow,c("epoch","dow","value")]
    dd[,"dowforecast"]=c(0,rollapply(dd[,"value"],cc,FUN=mean,align="right",fill=0,partial=1))[1:nrow(dd)]
    if(!plotted){
      plot(dd[,"epoch"],dd[,"value"],col=rainbow(max(d$dow))[dd$dow],main=paste("dowmodel",cc,title),pch=19,ylim=ylims)
      points(dd[,"epoch"],dd[,"dowforecast"],col=rainbow(max(d$dow))[dd$dow],main=paste("dowmodel",title))
#       plotted=T
    }else{
      points(dd[,"epoch"],dd[,"value"],col=rainbow(max(d$dow))[dd$dow],main=paste("dowmodel",cc,title),pch=19)
      points(dd[,"epoch"],dd[,"dowforecast"],col=rainbow(max(d$dow))[dd$dow],main=paste("dowmodel",title))
    }
    df=dd[,c("epoch","dowforecast")]
    if(!exists("fdf")) fdf=df else fdf=rbind(fdf,df)
  }
  print(cc)
  if(exists("fdf")) return(fdf)
}


metrics=read.table("metrics.csv",sep=",",header=T)
providers=read.table("providers.csv",sep=",",header=T)
observations=read.table("observations.csv",sep=",",header=T)
portfolios=read.table("portfolios.csv",sep=",",header=T)

observations=observations[,c("id","index","value","metrics_id")]
metrics=metrics[,c("id","name","providers_id")]
providers=providers[,c("id","provider_name","portfolios_id")]
portfolios=portfolios[,c("id","organizations_id")]

observations$epoch<-as.integer(as.POSIXct(observations$index))

colnames(metrics)[1]="metrics_id"
colnames(providers)[1]="providers_id"
colnames(portfolios)[1]="portfolios_id"

data=merge(
  merge(
    merge(
      observations,metrics,by="metrics_id")
    ,providers,by="providers_id")
  ,portfolios,by="portfolios_id")

data=data[order(data$epoch),]
row.names(data)=1:nrow(data)

groups=c(0:20)/20
# pdf("desciptive.pdf")
for(pid in sort(unique(data$portfolios_id))){
  obs=data[data[,"portfolios_id"]==pid,]
  organization=unique(obs$organizations_id)
  
  if(exists("pivotobs")) rm(list=c("pivotobs"))
  pdf(paste("org_",organization,".pdf",sep=""))
  for(mid in sort(unique(obs$metrics_id))){
    t=obs[obs[,"metrics_id"]==mid & obs[,"epoch"]<=1.4e9,]
    if(nrow(t)>1){
      ylims=c(as.numeric(min(t[,"value"])*.9),as.numeric(max(t[,"value"])*1.1))
      
      title=paste(paste(unique(t$provider_name),unique(t$name),sep="_"),paste(unique(t$providers_id),unique(t$metrics_id),sep="_"))
      plot(t[,"epoch"],t[,"value"],main=title,xlab="epoch",ylab="value",pch=19,col="black",ylim=ylims)   
      
      linmod=lm(t[,"value"]~t[,"epoch"])
      abline(linmod,col="red")
      t[,"groups"]=0
      qs=quantile(t[,"epoch"],probs=groups)
      for(q in 2:length(qs)){
        t[t[,"epoch"]<=qs[q] & t[,"groups"]==0,"groups"]=qs[q]
      }
      t[,"mean"]=ave(t[,"value"],t[,"groups"],FUN=mean)
      t[,"sd"]=ave(t[,"value"],t[,"groups"],FUN=sd)
      points(t[,"groups"],t[,"mean"],col="green",pch=19)
      points(t[,"groups"],t[,"sd"],col="orange",pch=19)
    #   points(t[,"groups"],t[,"mean"]+2*t[,"sd"],col="hotpink",pch=19)
    #   points(t[,"groups"],t[,"mean"]-2*t[,"sd"],col="indianred",pch=19)
    #   legend(x=(max(t[,"groups"])+10000),(max(t[,"value"])+50),c("value","fitted","mean","sd","upper","lower"))
    #   t[,"freq"]=ave(t[,"groups"],t[,"groups"],FUN=length)
    #   plot(t[,"groups"],t[,"freq"])
  #     fit=Mclust(t[,"value"],5)
  #     t[,"classification"]=fit$classification
      fit=kmeans(t[,"value"],min(length(unique(t[,"value"])),5))
      t[,"classification"]=fit$cluster
      t[,"center"]=fit$centers[fit$cluster]
  
      if(exists("sses")) rm(list=c("sses"))
      for(c in (4:8)){
        t[,"forecast"]=c(0,rollapply(t[,"center"],c,FUN=mean,align="right",fill=0,partial=1))[1:nrow(t)]
        plot(t[,"epoch"],t[,"value"],col=rainbow(max(t[,"classification"]))[t[,"classification"]],main=paste("cluster",c,title),ylim=ylims)
        points(t[,"epoch"],t[,"forecast"],col="black",pch=19)
        sse=calcSSE(t[,c("forecast","value")])
        ses=cbind(data.frame(c),sse)
        ses[,"type"]="clusteravg"
        if(!exists("sses")) sses=data.frame(ses) else sses=rbind(sses,ses)
      }
  
      plot(t[,"epoch"],t[,"value"],col=rainbow(max(unique(unclass(as.POSIXlt(t[,"index"]))$wday+1)))[unclass(as.POSIXlt(t[,"index"]))$wday+1],main=paste("dow",title),pch=19,ylim=ylims)
  
      cols=colnames(t)
      for(c in (1:5)){
        t=merge(t[,cols],dowmodel(t[,cols],c),by="epoch")
        sse=calcSSE(t[,c("dowforecast","value")])
        ses=cbind(data.frame(c),sse)
        ses[,"type"]="dowmodel"
        if(!exists("sses")) sses=data.frame(ses) else sses=rbind(sses,ses)
      }
      plot(t[,"epoch"],t[,"value"],col=rainbow(max(unique(unclass(as.POSIXlt(t[,"index"]))$mday)))[unclass(as.POSIXlt(t[,"index"]))$mday],main=paste("mday",title),pch=19,ylim=ylims)
      plot(t[,"epoch"],t[,"value"],col=rainbow(max(unique(unclass(as.POSIXlt(t[,"index"]))$mon+1)))[unclass(as.POSIXlt(t[,"index"]))$mon+1],main=paste("mon",title),pch=19,ylim=ylims)
      plot(t[,"epoch"],t[,"value"],col=rainbow(max(unique(unclass(as.POSIXlt(t[,"index"]))$hour+1)))[unclass(as.POSIXlt(t[,"index"]))$hour+1],main=paste("hour",title),pch=19,ylim=ylims)
  
  
      hist(t[,"epoch"],main=paste("epoch",title))
      hist(t[,"value"],main=paste("value",title)) 
      tt=t[,c("epoch","value")]
      colnames(tt)[2]=paste("col",unique(t$providers_id),unique(t$metrics_id),sep="_")
      if(!exists("pivotobs")) pivotobs=tt else pivotobs=merge(pivotobs,tt,by="epoch",all=T)
      if(exists("sses")) write.table(sses,file=paste("pivotobs/sses",mid,"_",organization,".txt",sep=""),sep="\t",row.names=F)
    }
  }
  cols=colnames(pivotobs)
  cols=cols[!(cols %in% "epoch")]
  op=par("mar")
  par(mar=rep(0,4))
  try(if(length(cols)>1) pairs(as.formula(paste("~",paste(cols,collapse="+"))),data=pivotobs,main=paste("pairs",organization)))
  for(prvid in unique(as.character(data.frame(strsplit(cols,"_"),stringsAsFactors=F)[2,]))){
    cols2=cols[grep(paste("_",prvid,"_",sep=""),cols,perl=T)]
    if(length(cols2)>1) pairs(as.formula(paste("~",paste(cols2,collapse="+"))),data=pivotobs,main=paste("pairs provider",prvid))
  }
  
  par(mar=op)
  dev.off()
  write.table(pivotobs,file=paste("pivotobs/pivotobs",organization,".txt",sep=""),sep="\t",row.names=F)
}
