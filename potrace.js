// PNG ---> SVG
const potrace = require("potrace");
const fs = require("fs");
const path = require("path");
const ProgressBar = require("progress");
// /mnt/data/llch/FontDiffuser/pic/cpp/ans
const inputDir = path.join(process.argv[2])|| path.join("D:\\aProject\\py\\FontDiffuser\\outputs\\cpp");
const outputDir = path.join(process.argv[3]) || path.join(__dirname, "svg_separate");

// 读取文件夹所有文件
fs.readdir(inputDir, function (err, files) {
  if (err) throw err;

  const pngFiles = files.filter(function (file) {
    return path.extname(file) === ".png";
  });

  const totalFiles = pngFiles.length;
  const progressBar = new ProgressBar("转换进度 [:bar] :percent :etas", {
    complete: "=",
    incomplete: " ",
    width: 50,
    total: totalFiles,
  });

  const startTime = Date.now(); // 记录时间

  function processFile(index) {
    if (index < totalFiles) {
      const file = pngFiles[index];
      const pngFilePath = path.join(inputDir, file);
      const svgFileName = path.basename(file, ".png") + ".svg";
      const svgFilePath = path.join(outputDir, svgFileName);

      // 使用 potrace 来转化 PNG 到 SVG
      potrace.trace(pngFilePath, function (err, svg) {
        if (err) throw err;
        fs.writeFileSync(svgFilePath, svg);

        // 更新进度条
        progressBar.tick();

        // 继续处理下一个文件
        processFile(index + 1);
      });
    } else {
      const endTime = Date.now(); // 记录完成时间
      const elapsedTime = (endTime - startTime) / 1000; // 耗时（秒）
      console.log("转换完成，共耗时:", elapsedTime.toFixed(2), "秒");
    }
  }

  processFile(0);
});
