// Program for Floyd Warshall Algorithm
#include <stdio.h>
#include <stdlib.h> 
// Number of vertices in the graph
#define V 1000
int num_vertices=-1, num_edges=-1;
/* Define Infinite as a large enough value. This value will be used
  for vertices not connected to each other */
#define INF 9999999

void printmatrix(int **graph)
{
	int i,j;
	for (i = 0; i < num_vertices; i++) {
        for (j = 0; j < num_vertices; j++) {
            printf("i:%d j:%d val:%d\n", i, j, graph[i][i]);
        }
    }
}
 
// Solves the all-pairs shortest path problem using Floyd Warshall algorithm
void floydWarshell (int **dist)
{
	int i,j,k;
    /* Add all vertices one by one to the set of intermediate vertices.
      ---> Before start of a iteration, we have shortest distances between all
      pairs of vertices such that the shortest distances consider only the
      vertices in set {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is added to the set of
      intermediate vertices and the set becomes {0, 1, 2, .. k} */
    for (k = 0; k < num_vertices; k++)
    {
        // Pick all vertices as source one by one
        for (i = 0; i < num_vertices; i++)
        {
            // Pick all vertices as destination for the
            // above picked source
            for (j = 0; j < num_vertices; j++)
            {
                // If vertex k is on the shortest path from
                // i to j, then update the value of dist[i][j]
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
}

FILE *fp;

// driver program to test above function
int main()
{
    int i=0,j=0;
    char line[100], member[100];
    //int graph[V][V];
	int **graph;
	int shortest_i=-1,shortest_j=-1, shortest_len=INF;

    fp = fopen("g1.txt", "r");
    if (fp == NULL)
           exit(1);

    fgets(line, 100, fp); // Read the first line
	printf("%s", line);
	for (i = 0, j = 0; i < 100; i++) {
		if(line[i] == ' ' || line[i] == '\0') {
			member[j] = '\0';
			j = 0;
			if(num_vertices == -1)
				num_vertices = atoi(member);
			else if (num_edges == -1)
				num_edges = atoi(member);
			else {
				printf("Error in num_Vertices line parsing %d\n", num_vertices);
				exit(-1);
			}
			if(line[i] == '\0')
				break;
		}
		else {
			member[j] = line[i];
			j++;
		}
    }
	printf("Number of vertices: %d\n", num_vertices);

	graph = (int**) malloc(num_vertices*(sizeof(int*)));
	if(!graph) {
        printf("Cannot alloc memory..Exiting\n");
        exit(-1);
    }
	for (i = 0; i < num_vertices; i++){
		graph[i] = (int *) malloc(num_vertices*sizeof(int));
		if(!graph[i]) {
	        printf("Cannot alloc memory..Exiting\n");
    	    exit(-1);
    	}
	}

	for(i = 0; i < num_vertices; i++)
        for(j = 0; j < num_vertices; j++) {
            if ( i == j)
                graph[i][j] = 0;
            else
                graph[i][j] = INF;
    }

	//printmatrix(graph);

    while (!feof(fp)) {
    	// Read file line by line
        fgets(line, 100, fp);
        // Line is of the form vertex1 vertex2 edge-cost
		int vertex1=-1, vertex2=-1, edge=-1;
        for (i = 0, j = 0; i < 100; i++) {
			if(line[i] == ' ' || line[i] == '\0') {
				member[j] = '\0';
				j = 0;
				if(vertex1 == -1)
					vertex1 = atoi(member);
				else if(vertex2 == -1)
					vertex2 = atoi(member);
				else if(edge == -1)
					edge = atoi(member);
				else {
					printf("Error in line parsing\n");
					exit(-1);
				}
				if(line[i] == '\0')
					break;
			}
			else {
				member[j] = line[i];
				j++;
			}
		}
		// Set entry in Graph
		//printf("vertex1: %d Vertex2: %d edge: %d\n", vertex1, vertex2, edge);
		graph[vertex1 -1][vertex2 - 1] = edge;
    }

    // compute
    floydWarshell(graph);

	// Detect if negative cycles
	for (i = 0; i < num_vertices; i++) {
		if(graph[i][i] < 0) {
			printf("Negative cycle exists\n");
			exit(0);
		}
	}

	// Print soln
	for (i = 0; i < num_vertices; i++) {
		for (j = 0; j < num_vertices; j++) {
			if(graph[i][j] < shortest_len) {
				shortest_i = i;
				shortest_j = j;
				shortest_len = graph[i][j];
			}
		}
	}
	printf("Shortest path is from %d to %d with len %d\n", (shortest_i+1),(shortest_j+1), shortest_len);
    return 0;
}
