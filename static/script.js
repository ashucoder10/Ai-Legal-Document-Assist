async function uploadPDF() {

    console.log("UPLOAD FUNCTION CALLED");

    const fileInput = document.getElementById("document-upload");

    if (fileInput.files.length === 0) {
        alert("No file selected");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML +=
`       <p><b>AI:</b> ${data.message}</p>`;

document.getElementById("pdfText").innerText = data.text || "";

    } catch (error) {
        console.error(error);
    }

}   


async function askAI() {

   const question = document.getElementById("question").value.trim();

if (question === "") {
    alert("Please enter a question.");
    return;
}

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: question
            })
        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML +=
        `<p><b>You:</b> ${question}</p>
         <p><b>AI:</b> ${data.reply}</p>`;
         const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;

    } catch (e) {
        console.log(e);
        alert("ERROR");
    }
    document.getElementById("question").value="";
}


async function analyzeResume() {

    document.getElementById("chatBox").innerHTML +=
    "<p><b>AI:</b> Reading Resume...</p>";

    try {

        const response = await fetch("/resume", {
            method: "POST"
        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML +=
        `<p><b>Resume Analysis:</b></p>
         <pre>${data.reply}</pre>`;

    } catch (e) {

        alert("Resume Error");

        console.log(e);

    }

}

async function analyzeReceipt() {

    try {

        const response = await fetch("/receipt", {
            method: "POST"
        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML += `
            <p><b>🧾 Receipt Analysis</b></p>
            <pre>${data.reply}</pre>
        `;

    } catch (e) {
        alert("Receipt Analysis Error");
        console.log(e);
  }
}

async function summarizeDocument() {

    try {

        const response = await fetch("/summary", {
            method: "POST"
        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML += `
            <p><b>📑 Document Summary</b></p>
            <pre>${data.reply}</pre>
        `;

    } catch (e) {

        alert("Summary Error");

        console.log(e);

    }
}

async function adjustDocumentSize() {

    const size = prompt("Enter size: small / medium / large");

    if (!size) return;

    try {

        const response = await fetch("/adjust-size", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                size: size.toLowerCase()
            })

        });

        const data = await response.json();

        document.getElementById("chatBox").innerHTML += `
            <p><b>📏 Adjusted Document (${size})</b></p>
            <pre>${data.reply}</pre>
        `;

    } catch (e) {

        alert("Adjust Size Error");

        console.log(e);

    }
} 

function showPDF(){

    const pdf=document.getElementById("pdfText");

    if(pdf.innerHTML===""){
        alert("Please upload a PDF first.");
        return;
    }

    if(pdf.style.display==="none"){
        pdf.style.display="block";
    }
    else{
        pdf.style.display="none";
    }

}