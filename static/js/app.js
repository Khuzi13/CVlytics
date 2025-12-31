const uploadArea = document.querySelector(".upload-area");
const fileInput = document.getElementById("fileElem");
const fileNameDisplay = document.getElementById("file-name-display");
const analyzeBtn = document.querySelector(".btn-block");

// Check if we are on the CV Checker page
if (uploadArea && fileInput) {
  // Click to upload
  uploadArea.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.addEventListener("change", function () {
    const file = this.files[0];
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (!file) return;

    // ❌ Not PDF
    if (file.type !== "application/pdf") {
    //   alert("You can upload PDF files only.");
    showToast("Only PDF files are allowed.", "error");

      this.value = "";
      return;
    }

    // ❌ Size greater than 5MB
    if (file.size > maxSize) {
    //   alert("File size 5MB se zyada hai");
    showToast("The file size must not exceed 5MB.", "error");
      this.value = "";
      fileNameDisplay.textContent = "";
      return;
    }

    // ✅ File valid
    fileNameDisplay.textContent = `Selected File: ${file.name}`;

    // ✅ BUTTON COLOR + TEXT (YEH WAHI CODE HAI)
    analyzeBtn.style.backgroundColor = "#4f46e5";
    analyzeBtn.textContent = "Analyze CV Now";

    // ✅ SHOW SUCCESS TOAST
    showToast(`Selected file: ${file.name}`, "success");
  });


  // Drag and Drop Effects (Optional Visuals)
  uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = "#4f46e5";
    uploadArea.style.backgroundColor = "#eff6ff";
  });

  uploadArea.addEventListener("dragleave", () => {
    uploadArea.style.borderColor = "#d1d5db";
    uploadArea.style.backgroundColor = "#f9fafb";
  });

  uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = "#d1d5db";
    uploadArea.style.backgroundColor = "#f9fafb";

    // Handle dropped file logic here if needed
    // alert("File dropped!");
  });
}

// ananana
// function analyzeCV() {
//   const file = fileInput.files[0];
//   const desc = document.querySelector("textarea").value;

//   if (!consentCheckbox.checked) {
//     showToast("Please agree to use your CV for anonymous model training before analyzing.", "warning");
//     return; // Stop further execution
//   }

//   if (!file) {
//     // alert("Please upload a PDF file first.");
//     showToast("Please upload a PDF file first.", "error");
//     return;
//   }

// showToast(
//   `Analyzing ${file.name}... Backend integration required for real AI analysis.`,
//   "info"
// );
// }

// function analyzeCV() {
//     const file = fileInput.files[0];
    
// // django variable 
//     // if (!vanishData) {
//     //     showToast("You cannot analyze CV at this time.", "warning");
//     //     return;
//     // }

//     // 1️⃣ Check if file uploaded
//     if (!file) {
//         showToast("Please upload a PDF file first.", "error");
//         return; // Stop execution
//     }

//     // 2️⃣ Check if user agreement checked
//     if (!consentCheckbox.checked) {
//         showToast(
//             "Please, enable user aggrement",
//             "warning" // warning color
//         );
//         return;
//     }

//     // 3️⃣ Both conditions satisfied → proceed
//     showToast(
//         `Analyzing ${file.name}... Backend integration required for real AI analysis.`,
//         "info"
//     );
// }


// new With Form file uploadation
// function analyzeCV() {
//     const file = fileInput.files[0];
//     const consentCheckbox = document.getElementById("consentCheckbox");
//     const form = document.getElementById("contactForm");

//     // 1️⃣ File check
//     if (!file) {
//         showToast("Please upload a PDF file first.", "error");
//         return;
//     }

//     // 2️⃣ User agreement check
//     if (!consentCheckbox.checked) {
//         showToast("Please agree to the user agreement first.", "warning");
//         return;
//     }

//     // 3️⃣ All OK → Submit form to Django
//     showToast("Uploading CV and analyzing...", "info");

//     // ⏳ Small delay so toast is visible
//     setTimeout(() => {
//         form.submit();
//     }, 800);
// }

function analyzeCV(event) {
    event.preventDefault(); // default submit roko

    const file = fileInput.files[0];
    const consentCheckbox = document.getElementById("consentCheckbox");
    const form = document.getElementById("contactForm");

    // 1️⃣ File check
    if (!file) {
        showToast("Please upload a PDF file first.", "error");
        return;
    }

    // 2️⃣ Agreement check
    if (!consentCheckbox.checked) {
        showToast("Please enable user agreement", "warning");
        return;
    }

    // 3️⃣ Success toast
    showToast("Uploading CV & analyzing...", "success");

    // 4️⃣ FORM SUBMIT (THIS WAS MISSING ❗)
    setTimeout(() => {
        form.submit();
    }, 800); // thora delay so toast visible rahe
}












// Hamburger Menu Toggle     1st -> Hamburger
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");

if (hamburger && navLinks) {
  hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("show");
  });
}

// Hamburger Menu Toggle with Animation     2st -> Hamburger
// const hamburger = document.getElementById("hamburger");
// const navLinks = document.getElementById("nav-links");

// if (hamburger && navLinks) {
//     hamburger.addEventListener("click", () => {
//         navLinks.classList.toggle("show");
//         hamburger.classList.toggle("active"); // ✅ Add this line for animation
//     });

//     // Close menu when clicking a link (optional)
//     const navItems = navLinks.querySelectorAll('a');
//     navItems.forEach(item => {
//         item.addEventListener('click', () => {
//             navLinks.classList.remove("show");
//             hamburger.classList.remove("active");
//         });
//     });
// }


// drag code

document.addEventListener("DOMContentLoaded", function () {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("fileElem");
  const fileNameDisplay = document.getElementById("file-name-display");

  if (!dropArea || !fileInput) return;

  // Click se file select
//   dropArea.addEventListener("click", () => fileInput.click());

  // Drag over
  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("drag-active");
  });

  // Drag leave
  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("drag-active");
  });

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("drag-active");

    const file = e.dataTransfer.files[0];
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (file.type !== "application/pdf") {
        // alert("You can upload only a PDF file.");
        showToast("Only PDF files are allowed.", "error");

        return;
    }

    if (file.size > maxSize) {
        // alert("The file size must not exceed 5MB.");
    showToast("The file size must not exceed 5MB.", "error");

        return;
    }

    fileInput.files = e.dataTransfer.files;
    fileNameDisplay.textContent = file.name;
    analyzeBtn.style.backgroundColor = "#4f46e5";
    analyzeBtn.textContent = "Analyze CV Now";
      // ✅ Success toast for drag/drop
    showToast(`Selected file: ${file.name}`, "success");
});

  // Normal select
  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      fileNameDisplay.textContent = fileInput.files[0].name;
    }
  });
});

// new showToast
function showToast(message, type = "info") {
    const toast = document.getElementById("toast");
    const toastMessage = document.getElementById("toast-message");

    if (!toast || !toastMessage) return;

    // Set icon and background based on type
    let iconClass = "fa-circle-info";
    let bgColor = "#1e3a8a"; // info default

    if (type === "success") {
        iconClass = "fa-circle-check";
        bgColor = "#065f46";
    } else if (type === "error") {
        iconClass = "fa-triangle-exclamation";
        bgColor = "#7f1d1d";
    } else if (type === "warning") {
        iconClass = "fa-triangle-exclamation";
        bgColor = "#d97706"; // yellow/orange
    }

    toast.className = `toast show`;
    toastMessage.textContent = message;
    toast.querySelector("i").className = `fa-solid ${iconClass}`;
    toast.style.background = bgColor;

    setTimeout(() => {
        toast.className = "toast";
    }, 3000);
}

  
  

//   User aggrement





// function showToast(message, type = "info") {
//   const toast = document.getElementById("toast");
//   const toastMessage = document.getElementById("toast-message");

//   if (!toast || !toastMessage) return;

//   // Set icon based on type
//   let iconClass = "fa-circle-info";
//   let bgColor = "#1e3a8a"; // info default

//   if (type === "success") {
//     iconClass = "fa-circle-check";
//     bgColor = "#065f46";
//   } else if (type === "error") {
//     iconClass = "fa-triangle-exclamation";
//     bgColor = "#7f1d1d";
//   } else if (type === "warning") {
//     iconClass = "fa-triangle-exclamation";
//     bgColor = "#d97706"; // yellow/orange
//   }

//   toast.className = `toast show`;
//   toastMessage.textContent = message;
//   toast.querySelector("i").className = `fa-solid ${iconClass}`;
//   toast.style.background = bgColor;

//   setTimeout(() => {
//     toast.className = "toast";
//   }, 3000);
// }


// EmailJS Initialization
emailjs.init("NgEFKewBpX5LSRg8w"); // Your Public Key

function sendMessage(event) {
    event.preventDefault();

    const templateParams = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        title: document.getElementById("subject").value,
        message: document.getElementById("message").value
    };

    emailjs.send("service_mxvkuya", "template_iva0zij", templateParams)
        .then(function(response) {
            console.log("SUCCESS!", response.status, response.text);
            document.getElementById("contactForm").reset();
            showToast("Message sent successfully!", "success");
        }, function(error) {
            console.log("FAILED...", error);
            showToast("Failed to send message. Check console.", "error");
        });
}


// Dark mode:
// ?????????
/* =========================
   DARK MODE TOGGLE
========================= */

// DOM Elements
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const themeText = document.getElementById('theme-text');

// Check for saved theme preference or default to 'light'
const savedTheme = localStorage.getItem('theme') || 'light';

// Apply saved theme on page load
document.documentElement.setAttribute('data-theme', savedTheme);
updateToggleButton(savedTheme);

// Toggle theme on button click
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        // Apply new theme
        document.documentElement.setAttribute('data-theme', newTheme);
        
        // Save preference
        localStorage.setItem('theme', newTheme);
        
        // Update button
        updateToggleButton(newTheme);
        
        // Show toast notification
        showToast(`${newTheme === 'dark' ? 'Dark' : 'Light'} mode activated`, 'info');
    });
}

// Update toggle button icon and text
function updateToggleButton(theme) {
    if (!themeIcon || !themeText) return;
    
    if (theme === 'dark') {
        themeIcon.className = 'fa-solid fa-sun';
        themeText.textContent = 'Light';
    } else {
        themeIcon.className = 'fa-solid fa-moon';
        themeText.textContent = 'Dark';
    }
}

// Optional: Detect system preference
function detectSystemTheme() {
    if (!localStorage.getItem('theme')) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const theme = prefersDark ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        updateToggleButton(theme);
    }
}

// Run on page load
detectSystemTheme();

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
        const theme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        updateToggleButton(theme);
    }
});

// // For Switch Toggle
// const themeSwitch = document.getElementById('theme-toggle');

// if (themeSwitch) {
//     // Set initial state
//     themeSwitch.checked = savedTheme === 'dark';
    
//     themeSwitch.addEventListener('change', () => {
//         const newTheme = themeSwitch.checked ? 'dark' : 'light';
//         document.documentElement.setAttribute('data-theme', newTheme);
//         localStorage.setItem('theme', newTheme);
//         showToast(`${newTheme === 'dark' ? 'Dark' : 'Light'} mode activated`, 'info');
//     });
// }





