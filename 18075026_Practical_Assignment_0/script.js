var AtbashWheel = {};

// Creating Atbash mapping for lowercase alphabets [a -> z, b -> y and... so on]
for(i = 65; i <= 90; i++)
{
  AtbashWheel[String.fromCharCode(i)] = String.fromCharCode(155 - i);
}
// Creating Atbash mapping for uppercase alphabets [A -> Z, B -> Y and... so on]
for(i = 97; i <= 122;i++)
{
  AtbashWheel[String.fromCharCode(i)] = String.fromCharCode(219 - i);
}

//This is used to call the Cipher function whenever text is written in the box
function checkInput(obj) {
  AtbashCipher(obj.value)
}

//Since it is a symmetric encryption, both encryption and decryption work identically
function AtbashCipher(txt){
  
  inputText = document.getElementById("input1").value;
  outputText = "";
  
  //Checking if inputText is empty
  if(inputText.length==0)
    document.getElementById("input2").value = "";
  
  for( i=0;i<inputText.length;i++)
  {
    // Checking if the character is an alphabet
    if( AtbashWheel[inputText[i]] !== undefined ) {
      //Use the character mapped throuh Atbash and stored in AtbashWheel
      outputText += AtbashWheel[inputText[i]];  
    }
    //Checking if the character is non alphabetic
    else {
      //No change, use the same character
      outputText += inputText[i];
    }
    document.getElementById("input2").value = outputText;
  }
}

var is_swapped = 0

function swapPlainAndCipher(){
  if(is_swapped == 0)
  {
    document.getElementById("input1").placeholder = "Cipher Text";
    document.getElementById("input2").placeholder = "Plain Text";
    document.getElementById("input1").value = "";
    document.getElementById("input2").value = "";
    document.getElementById("swap").innerHTML = "Change to Encryption";
  }
  else{
    document.getElementById("input1").placeholder = "Plain Text";
    document.getElementById("input2").placeholder = "Cipher Text";
    document.getElementById("input1").value = "";
    document.getElementById("input2").value = "";
    document.getElementById("swap").innerHTML = "Change to Decryption";
  }
  is_swapped ^= 1
}
