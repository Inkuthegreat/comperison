#simpson use for s and trapozoid use for t
def fn(x):
	result=3*pow(x,2)
	return result
f=open("comperison.txt","w")
a=1
b=2
header="n"+" "+"t_result"+" "+"s_result\n"
f.write(header)
for n in range(2,1000000,2):
	h=(b-a)/n
	d_val=a+h
	t_res=0
	i=1
	s_res=0
	main_result=7
	while d_val<b:
		t_res=t_res+fn(d_val)
		if i%2==0:
			s_res=s_res+2*fn(d_val)
		else:
			s_res=s_res+4*fn(d_val)
		d_val=d_val+h
		i+=1
	t_result=h*(t_res+(fn(a)+fn(b))/2)
	s_result=(h/3)*(fn(a)+fn(b)+s_res)
	t_error=abs(t_result-main_result)
	s_error=abs(s_result-main_result)
	err=str(n)+" "+str(t_error)+" "+str(s_error)+"\n"
	f.write(err)
