//*****************************************************************************
// Do not remove this notice.
//
// Copyright 2017 University of New Hapmshire by Dr. Alex Prusevich.
// alex.proussevitch@unh.edu
//*****************************************************************************
$(document).ready(function() {
  setInterval(function() {
    cache_clear()
  }, 300000);
});
// function create () {
// // $.ajax({
// // url:"check", //the page containing python script
// // type: "post", //request type,
// // dataType: 'json',
// // data: {registration: "success", name: "xyz", email: "abc@gmail.com"},
// // success:function(result){
// window.location.reload(true);
//       }
//     });
//    }md
function cache_clear() {

  window.location.reload(true);
  // window.location.reload(); use this if you do not remove cache
}

var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

$('.table-add').click(function () {
var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
$TABLE.find('table').append($clone);
});

$('.table-remove').click(function () {
$(this).parents('tr').detach();
});

$('.table-up').click(function () {
var $row = $(this).parents('tr');
if ($row.index() === 1) return; // Don't go above the header
$row.prev().before($row.get(0));
});

$('.table-down').click(function () {
var $row = $(this).parents('tr');
$row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {
var $rows = $TABLE.find('tr:not(:hidden)');
var headers = [];
var data = [];

// Get the headers (add special header logic here)
$($rows.shift()).find('th:not(:empty)').each(function () {
headers.push($(this).text().toLowerCase());
});

// Turn all existing rows into a loopable array
$rows.each(function () {
var $td = $(this).find('td');
var h = {};

// Use the headers from earlier to name our hash keys
headers.forEach(function (header, i) {
h[header] = $td.eq(i).text();
});

data.push(h);
});

// Output the result
$EXPORT.text(JSON.stringify(data));
});
