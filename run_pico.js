const fs = require("fs").promises;
const { exec } = require("child_process");
const util = require("util");
const asyncPool = require("tiny-async-pool");
const inputFolder = process.argv[2] || "./svg_separate";
const outputFolder = process.argv[3] || "./pico";
const concurrency = 20; // 同时执行的最大任务数量 太高可能导致 EBADF 错误
const execPromise = util.promisify(exec);
async function asyncPoolAll(...args) {
  const results = [];
  for await (const result of asyncPool(...args)) {
    results.push(result);
  }
  return results;
}

async function processFiles() {
  const startTime = Date.now();
  // Create output folder if it doesn't exist
  try {
    await fs.mkdir(outputFolder);
  } catch (err) {
    if (err.code !== "EEXIST") {
      console.error("Error creating output folder:", err);
      return;
    }
  }

  try {
    const files = await fs.readdir(inputFolder);
    await asyncPoolAll(concurrency, files, async (filename) => {
      try {
        await execPromise(
          `picosvg ${inputFolder}/${filename} > ${outputFolder}/${filename}`
        );
        console.log(
          `picosvg ${inputFolder}/${filename} > ${outputFolder}/${filename}`
        );
      } catch (err) {
        console.error(filename, `Error executing picosvg: ${err}`);
      }
    });
  } catch (err) {
    console.error("Error reading input folder:", err);
  }

  console.log("Conversion complete!");
  const endTime = Date.now();
  console.log("Time taken:", (endTime - startTime) / 1000, "seconds");
}

processFiles();
