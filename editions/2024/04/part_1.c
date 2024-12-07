#include <stdio.h>
#include <stdlib.h> // malloc
#include <string.h> // memset

char map[100*100];
char *rows[100];
int width, height;
int count;

char perm[4] = "XMAS";

inline void find_xmas(int x, int y, int dir_x, int dir_y)
{
	if (x + dir_x * 3 >= width)
		return;
	if (x + dir_x * 3 < 0)
		return;
	if (y + dir_y * 3 >= height)
		return;
	if (y + dir_y * 3 < 0)
		return;

	y += dir_y; x += dir_x;
	if (rows[y][x] != 'M')
		return;
	y += dir_y; x += dir_x;
	if (rows[y][x] != 'A')
		return;
	y += dir_y; x += dir_x;
	if (rows[y][x] != 'S')
		return;
	count++;
}

int main(int argc, char *argv[])
{
	if (argc < 2)
		return 1;

	FILE *fp = fopen("editions/2024/04/input.txt", "r");
	if (!fp)
		return 2;

	size_t UNUSED = fread(map, 1, sizeof(map) - 1, fp);
	fclose(fp);

	char *rn = strchr(map, '\r');
	char *nl = strchr(map, '\n');
	width = (rn ? rn : nl) - map;
	int increment = nl - map + 1;

	char *ptr = map;
	for (height = 0; *ptr; ++height, ptr += increment) {
		rows[height] = ptr;
		ptr[width] = 0;
	}

	for (int y = 0; y < height; ++y) {
		for (int x = 0; x < width; ++x) {
			find_xmas(x, y,  1,  0);
			find_xmas(x, y,  0,  1);
			find_xmas(x, y, -1,  0);
			find_xmas(x, y,  0, -1);

			find_xmas(x, y,  1,  1);
			find_xmas(x, y,  1, -1);
			find_xmas(x, y, -1,  1);
			find_xmas(x, y, -1, -1);
		}
	}

	printf("Count: %d\n", count);
	return 0;
}
