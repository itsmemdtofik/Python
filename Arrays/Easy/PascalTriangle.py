"""
     * !Pascal Triangle:
     *
     * Given an integer numRows, return the first numRows of Pascal's triangle.
     * In Pascal's triangle, each number is the sum of the two numbers directly
     * above it as shown:
     *
     * Example 1:
     * Input: numRows = 5
     * Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
     *
     * Example 2:
     * Input: numRows = 1
     * Output: [[1]]
    * !Row	    prevRow	    newRow Construction	                Output
       0	       -	        [1]	                            [[1]]
       1	      [1]	       [1, 1]	                        [[1], [1, 1]]
       2	      [1, 1]	  [1, 1+1, 1] → [1, 2, 1]	        [[1], [1, 1], [1, 2, 1]]
       3	      [1, 2, 1]	  [1, 1+2, 2+1, 1] → [1, 3, 3, 1]	[[1], [1,1], [1,2,1], [1,3,3,1]]

"""

def pascalTriangle(num_rows):

    triangle = []

    if num_rows == 0:
        return triangle

    #First Row
    triangle.append([1])

    for row_num in range(1, num_rows):
        prev_rows = triangle[row_num - 1]

        # First element is always one
        new_rows: list = [1]

        #Middle elements
        for j in range(1, row_num):
            new_rows.append(prev_rows[j - 1] + prev_rows[j])

        #Last element is always 1
        new_rows.append(1)

        triangle.append(new_rows)

    return triangle

number: int = 5
result = pascalTriangle(number)
for row in result:
    print(row)
