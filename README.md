# DS_HW1

# **資料預處理：**
    * 合成兩個資料集：台灣電力公司_過去電力供需資訊.csv與本年每日尖峰備轉容量率.csv
    * 將本年度每日尖峰備轉容量率中的備轉容量單位轉換成MW
    * 刪去兩個資料集重疊的日期資料
    * 訓練的資料取兩個欄位：日期與備轉容量率(MW)

# **模型建立：**
    使用facebook開發的時間序列預測模型Prophet
    模型架構如下：
        使用加法模型：y(t)=g(t)+s(t)+h(t)+ε(t)
         g(t)：趨勢的影響
         s(t)：季節性的影響
         h(t)：節日的影響
         ε(t)：誤差

### Trend
   ##### prophet使用兩種趨勢函數：
      1.Linear用於不飽和預測，公式如下：
 ![image](https://github.com/LinChiaWei/DS_HW/blob/main/images/4.png)
      
      2.Logistic用於飽和預測，公式如下：
   ![image](https://github.com/LinChiaWei/DS_HW/blob/main/images/5.png)      
   
   ##### 轉折點
      此外Prophet加入了轉折點(change point)的概念，讓趨勢函數在不同時間內有不同的成長率k，公式如下：
   ![image](https://github.com/LinChiaWei/DS_HW/blob/main/images/3.png) 
      
### Seasonlity
      prophet用傅立葉級數描述季節性，公式如下：
   ![image](https://github.com/LinChiaWei/DS_HW/blob/main/images/1.png) 
   
### Holiday
      將不同假日所造成的影響列入考量，公式如下：
   ![image](https://github.com/LinChiaWei/DS_HW/blob/main/images/2.png)    
    
