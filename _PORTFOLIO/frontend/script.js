// // Dark Mode Toggle
// const btn = document.getElementById('darkModeToggle');
// btn.addEventListener('click', () => {
//   document.body.classList.toggle('dark-mode');
//   btn.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
// });

// // Scroll Reveal
// const reveals = document.querySelectorAll(".reveal");

// function revealOnScroll() {
//   const windowHeight = window.innerHeight;
//   reveals.forEach((el) => {
//     const top = el.getBoundingClientRect().top;
//     if (top < windowHeight - 100) {
//       el.classList.add("active");
//     }
//   });
// }
// window.addEventListener("scroll", revealOnScroll);
// window.addEventListener("load", revealOnScroll);

// // Loader
// window.addEventListener("load", () => {
//   const loader = document.getElementById("loader-wrapper");
//   loader.style.opacity = "0";
//   loader.style.pointerEvents = "none";
//   setTimeout(() => loader.style.display = "none", 500);
// });

// // Chatbot with Real LLM Integration
// const chatbotToggle = document.getElementById("chatbot-toggle");
// const chatbotWindow = document.getElementById("chatbot-window");
// const chatbotClose = document.getElementById("chatbot-close");
// const chatbotInput = document.getElementById("chatbot-input");
// const chatbotMessages = document.getElementById("chatbot-messages");

// // Toggle chatbot window
// chatbotToggle.addEventListener("click", () => {
//   chatbotWindow.classList.toggle("hidden");
// });

// chatbotClose.addEventListener("click", () => {
//   chatbotWindow.classList.add("hidden");
// });

// // Message handling
// chatbotInput.addEventListener("keypress", function (e) {
//   if (e.key === "Enter" && chatbotInput.value.trim() !== "") {
//     const userMessage = chatbotInput.value.trim();
//     addMessage("user", "You", userMessage);
//     chatbotInput.value = "";
    
//     // Show typing indicator
//     addTypingIndicator();
    
//     // Send to backend
//     sendMessageToBackend(userMessage);
//   }
// });

// function addMessage(sender, label, text) {
//   const messageDiv = document.createElement("div");
//   messageDiv.classList.add("chat-message", sender);
//   const nameTag = `<strong>${label}:</strong><br>`;
//   messageDiv.innerHTML = nameTag + text;
//   chatbotMessages.appendChild(messageDiv);
//   chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
// }

// function addTypingIndicator() {
//   const typingDiv = document.createElement("div");
//   typingDiv.classList.add("chat-message", "chatbot", "typing");
//   typingDiv.id = "typing-indicator";
//   typingDiv.innerHTML = `<strong>Chatbot:</strong><br>Typing...`;
//   chatbotMessages.appendChild(typingDiv);
//   chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
// }

// function removeTypingIndicator() {
//   const typingDiv = document.getElementById("typing-indicator");
//   if (typingDiv) typingDiv.remove();
// }

// async function sendMessageToBackend(message) {
//   try {
//     // Try connecting to the backend
//     const response = await fetch('http://localhost:5000/api/chat', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ message: message })
//     });
    
//     removeTypingIndicator();
    
//     if (response.ok) {
//       const data = await response.json();
//       addMessage("chatbot", "Chatbot", data.response);
//     } else {
//       // Fallback if server is not running
//       addMessage("chatbot", "Chatbot", getFallbackResponse(message));
//     }
//   } catch (error) {
//     // If backend is not running, use fallback
//     removeTypingIndicator();
//     console.log("Backend not available, using fallback responses");
//     addMessage("chatbot", "Chatbot", getFallbackResponse(message));
//   }
// }

// // Fallback responses (works even without backend)
// function getFallbackResponse(message) {
//   const msg = message.toLowerCase();
  
//   if (msg.includes('skill') || msg.includes('know') || msg.includes('language')) {
//     return "💻 My technical skills include:\n\n• Languages: C, C++, Python\n• Web: HTML, CSS, JavaScript, Next.js\n• Database: MySQL\n• Tools: Git, MS Excel";
//   }
//   else if (msg.includes('project') || msg.includes('work') || msg.includes('built')) {
//     return "🚀 Here are my key projects:\n\n• Multi-Class Flower Classification (75.89% accuracy)\n• TCP Congestion Control Simulation\n• Hospital Management System\n• This interactive portfolio!";
//   }
//   else if (msg.includes('intern') || msg.includes('experience')) {
//     return "🎯 I interned at IIT Bhubaneswar (May-Jul 2025):\n\n• Developed AHRC Research Dashboard with Next.js\n• Implemented Twilio OTP authentication\n• Integrated real-time APIs";
//   }
//   else if (msg.includes('education') || msg.includes('study') || msg.includes('college')) {
//     return "📚 My education:\n\n• IIT Bhubaneswar: B.Tech CSE (2022-2026) - 6.77 CGPA\n• 12th: 92.9%\n• 10th: 10/10";
//   }
//   else if (msg.includes('contact') || msg.includes('email') || msg.includes('reach')) {
//     return "📬 Connect with me:\n\n• LinkedIn: linkedin.com/in/sagarika-devarakonda-298125278/\n• GitHub: github.com/DEVARAKONDASAGARIKA\n• Email: sagarikadevarakonda2004@gmail.com";
//   }
//   else {
//     return "🌟 I'd love to tell you about Sagarika! Ask about:\n• Skills & Languages\n• Projects & Work\n• Education\n• Experience\n• Contact info";
//   }
// }

// // Handle chat input with Enter key
// chatbotInput.addEventListener("keypress", function (e) {
//   if (e.key === "Enter" && chatbotInput.value.trim() !== "") {
//     const userMessage = chatbotInput.value.trim();
//     addMessage("user", "You", userMessage);
//     chatbotInput.value = "";
    
//     // Try backend first, fallback to local if not available
//     addTypingIndicator();
//     sendMessageToBackend(userMessage);
//   }
// });











// Dark Mode Toggle
const btn = document.getElementById('darkModeToggle');
btn.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  btn.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
});

// Scroll Reveal
const reveals = document.querySelectorAll(".reveal");

function revealOnScroll() {
  const windowHeight = window.innerHeight;
  reveals.forEach((el) => {
    const top = el.getBoundingClientRect().top;
    if (top < windowHeight - 100) {
      el.classList.add("active");
    }
  });
}
window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

// Loader
window.addEventListener("load", () => {
  const loader = document.getElementById("loader-wrapper");
  loader.style.opacity = "0";
  loader.style.pointerEvents = "none";
  setTimeout(() => loader.style.display = "none", 500);
});

// Chatbot with Real LLM Integration
const chatbotToggle = document.getElementById("chatbot-toggle");
const chatbotWindow = document.getElementById("chatbot-window");
const chatbotClose = document.getElementById("chatbot-close");
const chatbotInput = document.getElementById("chatbot-input");
const chatbotMessages = document.getElementById("chatbot-messages");

// Toggle chatbot window
chatbotToggle.addEventListener("click", () => {
  chatbotWindow.classList.toggle("hidden");
});

chatbotClose.addEventListener("click", () => {
  chatbotWindow.classList.add("hidden");
});

function addMessage(sender, label, text) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("chat-message", sender);
  const nameTag = `<strong>${label}:</strong><br>`;
  // Convert newlines to <br> tags
  const formattedText = text.replace(/\n/g, '<br>');
  messageDiv.innerHTML = nameTag + formattedText;
  chatbotMessages.appendChild(messageDiv);
  chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function addTypingIndicator() {
  const typingDiv = document.createElement("div");
  typingDiv.classList.add("chat-message", "chatbot", "typing");
  typingDiv.id = "typing-indicator";
  typingDiv.innerHTML = `<strong>Chatbot:</strong><br>Typing...`;
  chatbotMessages.appendChild(typingDiv);
  chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function removeTypingIndicator() {
  const typingDiv = document.getElementById("typing-indicator");
  if (typingDiv) typingDiv.remove();
}

async function sendMessageToBackend(message) {
  try {
    console.log("Sending message to backend...");
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: message })
    });
    
    console.log("Response status:", response.status);
    
    if (response.ok) {
      const data = await response.json();
      console.log("Response data:", data);
      removeTypingIndicator();
      addMessage("chatbot", "Chatbot", data.response);
    } else {
      removeTypingIndicator();
      addMessage("chatbot", "Chatbot", "Sorry, I couldn't connect to the server. Please try again later.");
    }
  } catch (error) {
    console.error("Error connecting to backend:", error);
    removeTypingIndicator();
    // Use fallback if backend not available
    const fallbackResponse = getFallbackResponse(message);
    addMessage("chatbot", "Chatbot", fallbackResponse);
  }
}

// Fallback responses (works even without backend)
function getFallbackResponse(message) {
  const msg = message.toLowerCase();
  
  if (msg.includes('skill') || msg.includes('know') || msg.includes('language')) {
    return "💻 My technical skills include:\n\n• Languages: C, C++, Python\n• Web: HTML, CSS, JavaScript, Next.js\n• Database: MySQL\n• Tools: Git, MS Excel";
  }
  else if (msg.includes('project') || msg.includes('work') || msg.includes('built')) {
    return "🚀 Here are my key projects:\n\n• Multi-Class Flower Classification (75.89% accuracy)\n• TCP Congestion Control Simulation\n• Hospital Management System\n• This interactive portfolio!";
  }
  else if (msg.includes('intern') || msg.includes('experience')) {
    return "🎯 I interned at IIT Bhubaneswar (May-Jul 2025):\n\n• Developed AHRC Research Dashboard with Next.js\n• Implemented Twilio OTP authentication\n• Integrated real-time APIs";
  }
  else if (msg.includes('education') || msg.includes('study') || msg.includes('college')) {
    return "📚 My education:\n\n• IIT Bhubaneswar: B.Tech CSE (2022-2026) - 6.77 CGPA\n• 12th: 92.9%\n• 10th: 10/10";
  }
  else if (msg.includes('contact') || msg.includes('email') || msg.includes('reach')) {
    return "📬 Connect with me:\n\n• LinkedIn: linkedin.com/in/sagarika-devarakonda-298125278/\n• GitHub: github.com/DEVARAKONDASAGARIKA\n• Email: sagarikadevarakonda2004@gmail.com";
  }
  else {
    return "🌟 I'd love to tell you about Sagarika! Ask about:\n\n• Skills & Languages\n• Projects & Work\n• Education\n• Experience\n• Contact info";
  }
}

// Handle chat input with Enter key
chatbotInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter" && chatbotInput.value.trim() !== "") {
    const userMessage = chatbotInput.value.trim();
    addMessage("user", "You", userMessage);
    chatbotInput.value = "";
    
    // Show typing indicator
    addTypingIndicator();
    
    // Try backend first, fallback to local if not available
    sendMessageToBackend(userMessage);
  }
});