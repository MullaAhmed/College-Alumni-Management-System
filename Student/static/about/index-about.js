document.getElementById("submit").onclick = function () {
  var disabled = document.getElementById("name").disabled;
  if (disabled) {
    document.getElementById("name").disabled = false;
  } else {
    document.getElementById("name").disabled = true;
  }

  var disabled = document.getElementById("name1").disabled;
  if (disabled) {
    document.getElementById("name1").disabled = false;
    document.getElementById("submit").style.backgroundColor = "#863dd9";
  } else {
    document.getElementById("name1").disabled = true;
    document.getElementById("submit").style.backgroundColor = "#333333";
  }

  var disabled = document.getElementById("name2").disabled;
  if (disabled) {
    document.getElementById("name2").disabled = false;
  } else {
    document.getElementById("name2").disabled = true;
  }

  var disabled = document.getElementById("name3").disabled;
  if (disabled) {
    document.getElementById("name3").disabled = false;
  } else {
    document.getElementById("name3").disabled = true;
  }

  var disabled = document.getElementById("name4").disabled;
  if (disabled) {
    document.getElementById("name4").disabled = false;
  } else {
    document.getElementById("name4").disabled = true;
  }

  var disabled = document.getElementById("name5").disabled;
  if (disabled) {
    document.getElementById("name5").disabled = false;
  } else {
    document.getElementById("name5").disabled = true;
  }

  var disabled = document.getElementById("name6").disabled;
  if (disabled) {
    document.getElementById("name6").disabled = false;
  } else {
    document.getElementById("name6").disabled = true;
  }

  var disabled = document.getElementById("name7").disabled;
  if (disabled) {
    document.getElementById("name7").disabled = false;
  } else {
    document.getElementById("name7").disabled = true;
  }

  var disabled = document.getElementById("name8").disabled;
  if (disabled) {
    document.getElementById("name8").disabled = false;
  } else {
    document.getElementById("name8").disabled = true;
  }

  var disabled = document.getElementById("name9").disabled;
  if (disabled) {
    document.getElementById("name9").disabled = false;
  } else {
    document.getElementById("name9").disabled = true;
  }

  var disabled = document.getElementById("name10").disabled;
  if (disabled) {
    document.getElementById("name10").disabled = false;
  } else {
    document.getElementById("name10").disabled = true;
  }

  var disabled = document.getElementById("file").disabled;
  if (disabled) {
    document.getElementById("file").disabled = false;
  } else {
    document.getElementById("file").disabled = true;
  }
};

// Upload-Image
const imgDiv = document.querySelector(".profile-pic-div");
const img = document.querySelector("#photo");
const file = document.querySelector("#file");
const uploadBtn = document.querySelector("#uploadBtn");

imgDiv.addEventListener("mouseenter", function () {
  uploadBtn.style.display = "block";
});

imgDiv.addEventListener("mouseleave", function () {
  uploadBtn.style.display = "none";
});

file.addEventListener("change", function () {
  const choosedFile = this.files[0];

  if (choosedFile) {
    const reader = new FileReader();

    reader.addEventListener("load", function () {
      img.setAttribute("src", reader.result);
    });

    reader.readAsDataURL(choosedFile);
  }
});
