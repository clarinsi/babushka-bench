from sklearn.metrics import classification_report,confusion_matrix
import sys
pred=[]
true=[]
for line in open(sys.argv[1]):
    line=line.strip().split('\t')
    if len(line)>1:
        pred.append(line[-1])
        true.append(line[-2])
print(classification_report(true,pred,digits=3))
#print(confusion_matrix(true[:17908],pred[:17908]))
def remove_prefix(lst):
	return ['-'.join(e.split('-')[1:]) for e in lst]
print(classification_report(remove_prefix(true),remove_prefix(pred),digits=3))
