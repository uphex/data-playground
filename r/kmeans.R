rm(list=ls())
loc="C:/Users/cjacobik/Desktop/Personal/uphex"
setwd(loc)

library(zoo)

numcluster=3

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

for(pid in sort(unique(data$portfolios_id))){
  obs=data[data[,"portfolios_id"]==pid,]
  organization=unique(obs$organizations_id)
  pdf(paste("org_",organization,".pdf",sep=""))
  for(mid in sort(unique(obs$metrics_id))){
    t=obs[obs[,"metrics_id"]==mid & obs[,"epoch"]<=1.41e9,]

    if(length(unique(t[,"value"]))>=(numcluster+1)){
      title=paste(paste(unique(t$provider_name),unique(t$name),sep="_"),paste(unique(t$providers_id),unique(t$metrics_id),sep="_"))
      ylims=c(as.numeric(min(t[,"value"])*.9),as.numeric(max(t[,"value"])*1.1))
      xlims=c(as.numeric(min(t[,"epoch"])),as.numeric(max(t[,"epoch"])))
      
      t[,"counter"]=c(1:nrow(t))
      if(exists("ftt")) rm(list=c("ftt"))
      for(i in (numcluster+1):nrow(t)){
        if(i%%as.integer(nrow(t)/3)==0){
          tt=t[t[,"counter"]<=i,]
          if(length(unique(tt[,"value"]))>=(numcluster+1)){
            fit=kmeans(tt[,"value"],numcluster)
            tt[,"classification"]=fit$cluster
            tt[,"center"]=fit$centers[fit$cluster]
            tt[,"sdvalue"]=sd(tt[,"value"])
            tt[,"diff"]=max(tt[,"center"])-min(tt[,"center"])
            tt[,"run"]=i
            tt=tt[,c("run","value","epoch","classification","center","sdvalue","diff")]
            plot(tt[,"epoch"],tt[,"value"],col=rainbow(max(tt[,"classification"]))[tt[,"classification"]],main=paste("cluster",i,title),ylim=ylims,xlim=xlims)
            for(center in unique(tt[,"center"])){
              abline(h=center)
            }
            if(!exists("ftt")) ftt=tt else ftt=rbind(ftt,tt)
          }
        }
        if(exists("ftt")) write.table(ftt,file=paste("tt/tt",pid,mid,"out.txt",sep="_"),row.names=F,sep="\t")
      }
    }      
  }
  dev.off()
}
