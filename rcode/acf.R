rm(list=ls())
loc="C:/Users/cjacobik/Desktop/Personal/uphex"
setwd(loc)

library(forecast)

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
  pdf(paste("arima_org_",organization,".pdf",sep=""))
  for(mid in sort(unique(obs$metrics_id))){
    t=obs[obs[,"metrics_id"]==mid & obs[,"epoch"]<=1.41e9,]    
    title=paste(paste(unique(t$provider_name),unique(t$name),sep="_"),paste(unique(t$providers_id),unique(t$metrics_id),sep="_"))
    ylims=c(as.numeric(min(t[,"value"])*.9),as.numeric(max(t[,"value"])*1.1))
      
    t[,"counter"]=c(1:nrow(t))
    xlims=c(as.numeric(min(t[,"counter"])),as.numeric(max(t[,"counter"])))
    
    sizeforecast=10
    minneeded=30
    for(i in minneeded:(nrow(t)-sizeforecast)){
      if(i%%as.integer(nrow(t)/20)==0){
        tt=t[t[,"counter"]<=i,]
        tt2=t[t[,"counter"]<=(i+sizeforecast) & t[,"counter"]>i,c("counter","value")]
        ts=ts(tt[,"value"])
#         plot.ts(ts,main=paste(i,title),xlim=xlims,ylim=ylims)
        arimamodel=auto.arima(ts,ic="bic")
        arimaforecast=forecast.Arima(arimamodel,h=10)
        plot.forecast(arimaforecast,main=paste(i,title),xlim=xlims,ylim=ylims)
        points(tt2[,"counter"],tt2[,"value"],col="red")
      }
    }     
  }
  dev.off()
}
