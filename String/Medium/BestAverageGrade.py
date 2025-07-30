"""
 * <pre>
 * !Best Average Grade:
 *
 * Given a list of student test score, find the best average grade.
 * Each student may have more than one test score in the list.
 * Complete the function BestAverageGrade funtion in the editor below.
 * It has only one parameter, scores, which is an array of students test scores.
 * Each elements in the array is a two-element array of the form [Student name, test score e.g.,["tofik",95].
 * test score may be positive and negative Integer.
 * If you end up with an average grade that is not integer, you use a floor
 * function to return the largest integer less than equal to the average.return 0
 * for empty input.
 *
 * Input:[{"bobby", 87},{"b", 100},{"B", 64},{"C",22}]
 * Expected Output is: 87
 *
 * Example Walkthrough:
 * For the input: { {"bobby", "87"}, {"b", "100"}, {"B", "64"}, {"C", "22"} }
 * Normalized names:
 * bobby -> bobby
 * b -> b
 * B -> b (normalized to lowercase)
 * C -> c
 *
 * Grouped scores:
 * bobby: [87] → Average = 87
 * b: [100, 64] → Average = (100 + 64) / 2 = 82
 * c: [22] → Average = 22
 * Maximum average: 87
 * Over All time complexity O(n)
 * </pre>
"""


def bestAverageGrade(scores: list[list[str]]) -> int:
    if scores is None or len(scores) == 0:
        return 0

    student_scores = {}

    for entry in scores:
        student = entry[0].lower()
        score = int(entry[1])

        if student not in student_scores:
            student_scores[student] = [0, 0]  # [totalScore, count]

        student_scores[student][0] += score
        student_scores[student][1] += 1

    max_average = float('-inf')

    for total_score, count in student_scores.values():
        average = int((total_score // count))  # Floor division as in Java
        max_average = max(max_average, average)

    return max_average


def main():
    scores = [
        ["bobby", "87"],
        ["b", "100"],
        ["B", "64"],
        ["C", "22"],
        ["D", "100"],
        ["E", "200"]
        # ["Bob", "87"], ["Mike", "35"], ["Bob", "52"], ["Jason", "35"],
        # ["Mike", "55"], ["Jessica", "99"]
    ]

    print("The best average score is :", bestAverageGrade(scores))  # Output: 87


if __name__ == "__main__":
    main()
