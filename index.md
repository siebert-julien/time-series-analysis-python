# TITLE
## Tasks definitions

time series analysis tasks are formally defined in the literature in time series data-mining reviews like [Fakhazari2017](#citation.fakhrazari2017),[Esling2012](#citation.esling2012),[Fu2011](#citation.fu2011),[Keogh2003](#citation.keogh2003).
Esling and Agon also define "implementation components" [Esling2012](#citation.esling2012)

### Indexing (query by content)

given a time series and some similarity measure, find the nearest matching time series.

### Clustering

find groups (clusters) of similar time series.

### Classification

assign a time series to a predefined class.

### Segmentation (Summarization)}

create an accurate approximation of a time series, by reducing its dimensionality while retaining its essential features.

### Forecasting (Prediction)

given a time series dataset up to a given time $t_n$, forecast the next values.

### Anomaly Detection

find abnormal data points or subsequences (also called discords).


### Motif Discovery

find every subsequences (called motif) that appears recurrently in a time series.

### Rules Discovery (Rule mining)

find the rules that may govern associations between sets of time series or subsequences \cite{Fu.2011,Fakhrazari.2017} 

## Implementation components

### preprocessing 
(e.g., filtering noise, removing outliers, or imputing missing values), 

### representation (e.g., dimensionality reduction, finding fundamental shape characteristics), 

### similarity measures, 

### indexing schemes.

## References

<a name="citation.esling2012">1.</a> Esling, P., Agon, C.: Time-series data mining. ACM Computing Surveys 45(1), 1{34 (2012). https://doi.org/10.1145/2379776.2379788

<a name="citation.fakhrazari2017">2.</a> Fakhrazari, A., Vakilzadian, H.: A survey on time series data mining. In: 2017 IEEE International Conference on Electro Information Technology (EIT). pp. 476{481. IEEE (5/14/2017 - 5/17/2017). https://doi.org/10.1109/EIT.2017.8053409

<a name="citation.fu2011">3.</a> Fu, T.c.: A review on time series data mining. Engineering Applications of Artificial Intelligence 24(1), 164{181 (2011). https://doi.org/10.1016/j.engappai.2010.09.007

<a name="citation.keogh2003">4.</a> Keogh, E., Kasetty, S.: On the Need for Time Series Data Mining Benchmarks: A Survey and Empirical Demonstration (2003)
