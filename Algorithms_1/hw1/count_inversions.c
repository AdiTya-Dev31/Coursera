#include <stdio.h>
#include <stdlib.h>

#define INPUT_SIZE 5

int Merge(int *array, int left, int mid, int right)
{
        /*We need a Temporary array to store the new sorted part*/
        int tempArray[right-left+1];
	int i_count=0;	
        int pos=0,lpos = left,rpos = mid + 1;
	int lsize=mid-left+1;
        while(lpos <= mid && rpos <= right)
        {
                if(array[lpos] < array[rpos])
                {
                        tempArray[pos++] = array[lpos++];
                }
                else
                {
                        tempArray[pos++] = array[rpos++];
			// increment i_count by lsize-lpos
			i_count += lsize-lpos;
                }
        }
        while(lpos <= mid)  tempArray[pos++] = array[lpos++];
        while(rpos <= right)tempArray[pos++] = array[rpos++];
        int iter;
        /* Copy back the sorted array to the original array */
        for(iter = 0;iter < pos; iter++)
        {
                array[iter+left] = tempArray[iter];
        }
        return i_count;
}

int merge(int arr[], int left, int mid, int right)
{
  int i, j, k;
  int temp[INPUT_SIZE];
  int inv_count = 0;
 
  i = left; /* i is index for left subarray*/
  j = mid;  /* i is index for right subarray*/
  k = left; /* i is index for resultant merged subarray*/
  while ((i <= mid - 1) && (j <= right))
  {
    if (arr[i] <= arr[j])
    {
      temp[k++] = arr[i++];
    }
    else
    {
      temp[k++] = arr[j++];
 
     /*this is tricky -- see above explanation/diagram for merge()*/
      inv_count = inv_count + (mid - i);
    }
  }
 
  /* Copy the remaining elements of left subarray
   (if there are any) to temp*/
  while (i <= mid - 1)
    temp[k++] = arr[i++];
 
  /* Copy the remaining elements of right subarray
   (if there are any) to temp*/
  while (j <= right)
    temp[k++] = arr[j++];
 
  /*Copy back the merged elements to original array*/
  for (i=left; i <= right; i++)
    arr[i] = temp[i];
 
  return inv_count;
}

int MergeSort(int *array, int left, int right)
{
        int mid = (left+right)/2;
	int x=0,y=0,z=0;
        /* We have to sort only when left<right because when left=right it is anyhow sorted*/
        if(left<right)
        {
                /* Sort the left part */
                x = MergeSort(array,left,mid);
                /* Sort the right part */
                y = MergeSort(array,mid+1,right);
                /* Merge the two sorted parts */
                z = merge(array,left,mid,right);
        }
	return x+y+z;
}

int main(void) {
	FILE *fp;
	int array[INPUT_SIZE];
	int i;
	int i_count;

	fp = fopen("/home/ashish/coursera/algos/trial.txt", "r");

	if(!fp) {
		printf("could not open file\n");
	}

	for(i=0; i < INPUT_SIZE; i++) {
		// read input from file
		fscanf(fp, "%d", &array[i]);
		printf("%d: %d\n", i, array[i]);
	}

	i_count = MergeSort(array,0,INPUT_SIZE-1);	
	printf("number of inversions = %d\n", i_count);
	return 0;
}


