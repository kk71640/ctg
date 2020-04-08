# CTG
CTG(胎児心拍陣痛図) dataを用いた解析用のリポジトリ

## CTU-CHB dataset
Open access CTG dataset

https://physionet.org/content/ctu-uhb-ctgdb/1.0.0/

The CTG recordings start no more than 90 minutes before actual delivery, and each is at most 90 minutes long. Each CTG contains a fetal heart rate (FHR) time series and a uterine contraction (UC) signal, each sampled at 4 Hz.

- inclusion criteria
    - Singleton pregnancy
    - Gestational age >36 weeks
    - No a priori known developmental defects
    - Duration of stage 2 of labor ≤ 30 minutes
    - FHR signal quality (i.e. percentage of the recording during which FHR data were available) > 50% in each 30 minute window
    - Available analysis of biochemical parameters of umbilical arterial blood sample (i.e. pH)
    - Majority of vaginal deliveries (only 46 cesarean section (CS) deliveries included)

### data description

|UApH|N|
|:---:|:---:|
|< 7.05|40|
|≥ 7.05|512|

## 参考
http://people.ciirc.cvut.cz/~spilkjir/matlab.html
