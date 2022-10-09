let runButton = document.getElementById("runBtn"); 

// Setup 
let codeEditor = ace.edit('jsEditor')

// Default code 
const defaultCode = 'console.log("Welcome to Creator Dev");';

// output dev
var outputDisplay = document.getElementById("output")

let editorLib = {
  init(){
    // Configure Editor 


    // Theme
    codeEditor.setTheme("ace/theme/xcode");

    // Set Language
    codeEditor.session.setMode("ace/mode/javascript")


    // Set Options
    codeEditor.setOptions({
      fontFamily:'code',
      fontSize : '16px',  
      enableBasicAutoCompletion:true,
      enableLiveAutoCompletion:true,
    })


    // set Default
    codeEditor.setValue(defaultCode);
  }
}
 
// run Code Btn
runButton.addEventListener('click',()=>{
  const userCode = codeEditor.getValue();

  // run the use code
  try {
    var result = new Function(userCode)();
    console.log(result);
    outputDisplay.innerHTML = result;
  } catch (error) {
    console.log(error);
  }
})


editorLib.init()