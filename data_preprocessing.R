library(dplyr)
{
  right = function(text, num_char) {
    substr(text, nchar(text) - (num_char-1), nchar(text))
  }
  minmax = function(x){
    (x-min(x))/(max(x)-min(x))
  } 
}

top50 <- c('091990','215600','035760','084990','003670','086900','028300',
           '253450','263750','025980','068760','034230','036490','078340',
           '145020','095700','056190','046890','041960','028150','003380',
           '098460','041510','042000','192080','035900','178920','022100',
           '036830','038540','048260','240810','102940','000250','066970',
           '122870','183490','140410','058470','086520','036420','092040',
           '083790','069080','200230','030190','073070','007390','267980')


# set directory to your own path
list <- list.files(path='C:/Users/CHO/Desktop/stockdata/golden')  

final_list <- vector()  

for(i in 1:length(top50)){
  a <- grep(top50[i],list)
  final_list <- c(final_list,a)
}

final_index <- list[final_list]
final_index <- setdiff(final_index,'102940_2019-04-01.txt')


setwd('C:/Users/CHO/Desktop/stockdata/golden')



for(k in 338:length(final_index)){
  print(k)
  name <- final_index[k]
  ddate <- substr(name,8,17)
  a <- read.table(name, stringsAsFactors = T)
  a$V44 <- NULL 
  
  # define the column name
  colnames(a) <- c("jongmok",'time','accum_vol','md10','md10_vol','md9','md9_vol','md8','md8_vol',
                   'md7','md7_vol','md6','md6_vol','md5','md5_vol','md4','md4_vol','md3','md3_vol',
                   'md2','md2_vol','md1','md1_vol','ms1','ms1_vol','ms2','ms2_vol','ms3','ms3_vol',
                   'ms4','ms4_vol','ms5','ms5_vol','ms6','ms6_vol','ms7','ms7_vol','ms8','ms8_vol',
                   'ms9','ms9_vol','ms10','ms10_vol')
  
  
  {
    jongmok <- gsub("\\[|\\]", "", as.character(a$jongmok[1]))
    jongmok <- gsub("'", "", jongmok)
    a <- a[-1]
    
    b <- data.frame()
    b <- lapply(a, abs) #시작가 기준 수익률로 인해 발생하는 - 부호 제거
    b <- as.data.frame(b)
    
    b <- subset(b, time >91000) #장 시작 전 동시호가 제외,
    b <- subset(b, time <152000) #장마감 동시호가 제외, 증권시장 정규시간만 대상
    
    # 초 단위 분석을 위해 똑같은 sec의 데이터 중 마지막 tick만을 선택
    b <- b[!duplicated(b[,'time'],fromLast = TRUE),]
    time2 <- c(b$time[1]:b$time[nrow(b)])
    time2_last <- right(time2,2)
    time2_mid <- right(time2,4)
    time2_basket <- substr(time2_mid,1,2)
    time_index <- (1:length(time2))
    time_table <- as.data.frame(cbind(time_index, time2, as.numeric(time2_last), as.numeric(time2_basket)))
    
    time_table_sub <- subset(time_table, V3 <60)
    time_table_sub <- subset(time_table_sub, V4 <60)
    time_table_final <- as.data.frame(time_table_sub$time2)
    colnames(time_table_final) <- 'time'
    dataset <- left_join(time_table_final, b, by='time')
    dataset2 <- dataset
    final_time <- dataset2$time  
  }
  
  
  # 일정한 sec 단위 분석을 위해 NULL값인 sec에 이전 sec 데이터 입력
  for(i in 2:nrow(dataset2)){
    #print(i)
    if(is.na(dataset2[i,]$md10)==TRUE){
      dataset2[i,] <- dataset2[i-1,]
    }
  }
  
  dataset2$time <- final_time
  
  b <- dataset2
  
  ttest1 <- data.frame()
  ttest2 <- data.frame()
  ttest3 <- data.frame()
  
  for(i in 1:(nrow(b)-18)){
    
    if(b$md8[i+18]>b$md8[i+9]){
      ttest1 <- rbind(ttest1,b[i:(i+9),]) # 상승
      
    }else if(b$md8[i+18]<b$md8[i+9]){
      ttest2 <- rbind(ttest2,b[i:(i+9),]) # 하락
    }else{
      #ttest3 <- rbind(ttest3,b[i:(i+9),]) # 보합
    }
  }
  
  indice_0 <- sample(1:(nrow(ttest1)/10),min((nrow(ttest1)/10),(nrow(ttest2)/10)),replace = FALSE)
  indice_0_t <- 10*indice_0
  indice_1 <- sample(1:(nrow(ttest2)/10),min((nrow(ttest1)/10),(nrow(ttest2)/10)),replace = FALSE)
  indice_1_t <- 10*indice_1
  
  basket1 <- data.frame()
  basket2 <- data.frame()
  
  for(i in 1:min((nrow(ttest1)/10),(nrow(ttest2)/10))){
    basket1 <- rbind(basket1, ttest1[(indice_0_t[i]-9):indice_0_t[i],])
    basket2 <- rbind(basket2, ttest2[(indice_1_t[i]-9):indice_1_t[i],])
  }
  
  basket1 <- basket1[c(4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42)]
  basket2 <- basket2[c(4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42)]
  
  final <- rbind(basket1,basket2)
  
  #prepr <- final/rowSums(final)
  
  # set directory to your own path
  write.csv(final,paste("C:/Users/CHO/Desktop/10_9_data/",jongmok,"_",ddate,"_10_9_refine.csv",sep =''),row.names = F)
}

