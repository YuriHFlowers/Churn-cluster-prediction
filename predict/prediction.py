from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn_extra.cluster import KMedoids


def predic_pres(results):

    if results == 0:
        op1 = "Cluster 1"
        op2 = "This client is very likely to continue with the service!"
        img = "cluster1.png"

    elif results == 1:
        op1 = "Cluster 2"
        op2 = "This client is likely to continue with the service!"
        img = "cluster2.png"

    elif results == 2:
        op1 = "Cluster 3"
        op2 = "This customer is likely to be Churned!"
        img = "cluster3.png"

    else:
        op1 = "Cluster 4"
        op2 = "This client is likely to continue with the service"
        img = "cluster4.png"

    return op1, op2, img
