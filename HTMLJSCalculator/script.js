document
  .getElementById("calcForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Get input values
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;
    let result;

    // Perform the calculation
    switch (operation) {
      case "add":
        result = num1 + num2;
        break;
      case "subtract":
        result = num1 - num2;
        break;
      case "multiply":
        result = num1 * num2;
        break;
      case "divide":
        if (num2 !== 0) {
          result = num1 / num2;
        } else {
          result = "Error: Division by zero";
        }
        break;
      default:
        result = "Error: Invalid operation";
    }

    // Display the result
    document.getElementById("result").textContent = `Result: ${result}`;
  });
