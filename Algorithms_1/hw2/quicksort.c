#include <stdio.h>
#include <stdlib.h> 

int count=0;
const int MAX_ELEMENTS = 10000;
int count1=0;
int count2=0;
int count3=0;
int count1a=0;
int count2a=0;

//Swaps two numbers at indices 'i' and 'j' in the array pointed by 'a'
void swap(int* a,int i,int j)
{
    int t;
    t=a[i];
    a[i]=a[j];
    a[j]=t;
} 

int choose_pivot(int *a, int l,int r )
{
    // find middle element
    int mid;
    int mini, maxi;

    mid = (l+r)/2;
    // find median between a[l], a[mid] and a[r]
    if(a[l] < a[mid]) {
	mini = l;
    }
    else {
  	mini = mid;
    }
    if(a[r] < a[mini]) {
	mini = r;
    }

    if(a[l] > a[mid]) {
	maxi = l;
    }
    else {
	maxi = mid;
    }
    if(a[r] > a[maxi]) {
	maxi = r;
    }

    // now return index of median
    if ( l == mini && r == maxi)
	return mid;
    else if ( l == mini && mid == maxi)
	return r;
    else if ( mid == mini && r == maxi)
	return l;
    else if ( mid == mini && l == maxi)
	return r;
    else if ( r == mini && l == maxi)
	return mid;
    else if( r == mini && mid == maxi)
	return l;
}

//Supporting routine for Quicksort
int partition_clrs(int* a,int l,int r)
{
    int i,j; 
    int x;
    int len= r-l;

    x = a[r];
    i = l-1;
    count1a = count1a + len;
    for(j=l;j<r;j++)
    {
        if(a[j] <= x)        
        {
            i++;
            swap(a,i,j);
        }
	count2a++;	
    }        
    swap(a,i+1,r);
    return(i+1);
}

//Supporting routine for Quicksort
int partition(int* a,int l,int r)
{
    int i,j;
    int x;
    int len = r-l;

    //swap(a,l,r);  // This is for part 2. For part 1 comment this line out

    // part 3
    int pivot = choose_pivot(a, l, r);
    swap(a, l, pivot);

    x = a[l];
    i = l+1;
    count1 = count1 + len;
    for(j=l+1;j<r+1;j++)
    {
        if(a[j] <= x)
        {
            swap(a,i,j);
	    i++;
        }
	count2++;
    }
    
    swap(a,i-1,l);
    return(i-1);
}

void quicksort(int *a,int l,int r,int length)
{
    int q;
    //int k;
    if(l>=r)
        return;
    else
    {
	count3 = count3 + r - l;
	/*printf("PASS %d: count1=%d count2=%d count3=%d\n",++count, count1, count2, count3);
	for(k=0;k<length;k++)
		printf("%d ",a[k]);
	printf("\n");*/

	q = partition(a,l,r);
        quicksort(a,l,q-1, length);
        quicksort(a,q+1,r, length);
    }
}

void printlist(int list[],int n)
{
   int i;
   for(i=0;i<n;i++)
      printf("%d\t",list[i]);
   printf("\n");
}

int main()
{
   int list[MAX_ELEMENTS];
   int i = 0;
   FILE *fp;

   fp = fopen("/home/ashish/coursera/algos/hw2/QuickSort.txt", "r");

   if(!fp) {
      printf("could not open file\n");
   }

   for(i=0; i < MAX_ELEMENTS; i++) {
      // read input from file
      fscanf(fp, "%d", &list[i]);
   }
  
 
   // sort the list using quicksort
   quicksort(list,0,MAX_ELEMENTS-1, MAX_ELEMENTS);

   // print the result
   printf("The list after sorting using quicksort algorithm:\n");
   printlist(list,MAX_ELEMENTS);
   printf("Number of comparisons: count1=%d count2=%d count3=%d\n", count1, count2, count3);
   printf("Number of comparisons: count1a=%d count2a=%d count3=%d\n", count1a, count2a, count3);
   
   return 0;
}

