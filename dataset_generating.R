# set directory to your own path
list <- list.files('C:/Users/CHO/Desktop/주식_틱_데이터/10_10_data')
jongmok <- unique(substr(list,1,6))

for(k in 1:49){
  print(k)
  
  scope <- grep(jongmok[k],list)
  target <- list[scope]
  basket_up <- data.frame()
  basket_down <- data.frame()
  
  UP <- data.frame()
  DOWN <- data.frame()
  UP_test <- data.frame()
  DOWN_test <- data.frame()
  
  for(i in 1:as.integer(0.7*length(scope))){
    # set directory to your own path
    a <- read.csv(paste('C:/Users/CHO/Desktop/주식_틱_데이터/10_10_data/',target[i],sep = ''))
    basket_up <- a[1:(0.5*nrow(a)),]
    basket_down <- a[((0.5*nrow(a))+1):nrow(a),]
    UP <- rbind(UP,basket_up)
    DOWN <- rbind(DOWN,basket_down)
    
  }
  for(i in (as.integer(0.7*length(scope))+1):length(scope)){
    # set directory to your own path
    a <- read.csv(paste('C:/Users/CHO/Desktop/주식_틱_데이터/10_10_data/',target[i],sep = ''))
    basket_up <- a[1:(0.5*nrow(a)),]
    basket_down <- a[((0.5*nrow(a))+1):nrow(a),]
    UP_test <- rbind(UP_test,basket_up)
    DOWN_test <- rbind(DOWN_test,basket_down)
  }
  
  train <- rbind(UP,DOWN)
  
  test <- rbind(UP_test,DOWN_test)
  
  # set directory to your own path
  write.csv(train,paste('C:/Users/CHO/Desktop/주식_틱_데이터/10_10_dataset/',jongmok[k],'_train.csv',sep = ''),row.names = F)
  # set directory to your own path
  write.csv(test,paste('C:/Users/CHO/Desktop/주식_틱_데이터/10_10_dataset/',jongmok[k],'_test.csv',sep = ''),row.names = F)
  
  
}





