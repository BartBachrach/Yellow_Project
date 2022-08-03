d3.selectAll("body").on("change", updatePage);
// this line uses the d3.selectAll() method to create an event listener
// whenever there is a change to the HTML body, the updatePage() function is called
// that is, when an event occurs on the page, such as a selection of a dropdown menu option,
// the updatePage() function is triggered

function updatePage() {
    let dropdownMenu = d3.selectAll("#selectOption").node();
    // it defines the dropdown menu with d3.selectAll and passes in the HTML id of the dropdown menu
    let dropdownMenuID = dropdownMenu.id;
    // the ID of the dropdown menu is assigned to the variable dropdownMenuID (dropdown menu was previously defined as "#selectOption" from it's HTML id)
    let selectedOption = dropdownMenu.value;
    // whenenver a dropdown option is selected, it's value is assigned the variabel "selectedOption". Note, selectOption is the id value of the dropdown menu
    // while selectEDOption is the option that is chosen by the user

    console.log(dropdownMenuID);
    console.log(selectedOption);
    // each time updatePage() is triggered, the "id" value of the dropdown menu, as well as the menu option
    // are printed to the console
};

// OR
// Getting a reference to the button on the page with the id property set to `click-me`
let button1 = d3.select("#exampleSelect1");
let button2 = d3.select("#exampleSelect2");
let button3 = d3.select("#exampleSelect3");

// Getting a reference to the input element on the page with the id property set to 'input-field'
let inputField = d3.select("#input-field");

// This function is triggered when the button is clicked
function handleClick() {
  console.log("Hi, button1 was clicked!");

  // We can use d3 to see the object that dispatched the event
  console.log(d3.event.target);
}

// We can use the `on` function in d3 to attach an event to the handler function
button1.on("click", handleClick);

// You can also define the click handler inline
button2.on("click", function() {
  console.log("Hi, button2 was clicked!");
  console.log(d3.event.target);
});

// Event handlers are just normal functions that can do anything you want
button3.on("click", function() {
  console.log("Hi, button3 was clicked!");
  console.log(d3.event.target);
  d3.select(".giphy-me").html("<img src='https://gph.to/2Krfn0w' alt='giphy'>");
});

// Input fields can trigger a change event when new text is entered.
inputField.on("change", function() {
  var newText = d3.event.target.value;
  console.log(newText);
});
