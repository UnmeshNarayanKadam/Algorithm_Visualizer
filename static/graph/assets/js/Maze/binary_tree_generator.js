/** Class for generating a maze using the binary tree generator.
 * The maze generated by this class can be represented as a binary tree.
 */
class BinaryTreeGenerator {
  constructor() {}

  /**
   * Fills the grid with walls as preparation for the algorithm.
   */
  fillGrid() {
    for (let y = 0; y < gridData.length; y++) {
      for (let x = 0; x < gridData[y].length; x++) {
        gridData[y][x].type = "wall";
        d3.select("#node-" + y + "-" + x)
          .transition()
          .duration(500)
          .attr("fill", "#171717");
      }
    }
  }

  /**
   * Function for running the binary tree generator.
   * Loops over the whole grid and generates the maze row by row.
   */
  async startMaze() {
    // fill the grid so the algorithm can carve the paths
    this.fillGrid();

    for (let y = 1; y < gridData.length - 1; y += 2) {
      for (let x = 1; x < gridData[y].length - 1; x += 2) {
        let dirs = [];

        // adding the directions the algorithm can carve
        // the path in to an array.
        if (y > 1) {
          // carve upwards
          dirs.push({ y: y - 1, x });
        }
        if (x < gridData[y].length - 2) {
          // carve right
          dirs.push({ y: y, x: x + 1 });
        }

        // set the current cell to type "floor"
        gridData[y][x].type = "floor";
        await colorBlock("#node-" + y + "-" + x, "#FFFFFF", 100, 10);

        // The last cell in the first row has no direction to carve in.
        // It is the only cell where the length of the dirs array is 0.
        if (dirs.length != 0) {
          // randomly choose a direction
          let taken = dirs.length > 1 ? Math.round(Math.random()) : 0;
          var direction = dirs[taken];

          // update the cell in the direction that was chosen earlier
          gridData[direction.y][direction.x].type = "floor";
          await colorBlock(
            "#node-" + direction.y + "-" + direction.x,
            "#FFFFFF",
            100,
            10
          );
        }
      }
    }
  }
}
