"""
     * <pre>
     * !Walking Rebot:
     *
     * Instructions:Implement the walk method. this method takes in a string path
     * where each character in the string corresponds to a potential movements of the robot.
     * the robot can move up, down, left and right represented by the character 'U','D','L' and 'R' respectively.
     * All other character may be ignored.
     *
     * Assume the robot's initial position is at (0,0).
     * The output of this method is the robot's final x and y cordinates relative
     * to the initial position.
     *
     * !Approach:
     * Step1: Initialize the robot's position at (0, 0)
     * Step2: ltervate over each character in the path
     * Step3: Move up, Move Down, Move left, Move right
     * Step4: Ignore other character
     * </pre>
"""


def walk(path: str) -> list[int]:
    x = 0
    y = 0

    for move in path:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1

    return [x, y]


if __name__ == "__main__":
    path = "ULDR"
    result = walk(path)
    print(result)  # Expected output: [0, 0]
