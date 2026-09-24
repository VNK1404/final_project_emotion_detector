function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    $.get("/emotionDetector", { textToAnalyze: textToAnalyze }, function (data) {
        document.getElementById("system_response").innerText = data;
    });
}
