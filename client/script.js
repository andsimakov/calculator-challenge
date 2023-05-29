$(document).ready(function() {
    $("#calculateButton").click(function() {
        var operands = [];
        var operators = [];

        var operand1 = parseInt($("#operand1").val());
        var operand2 = parseInt($("#operand2").val());
        var operator = $("#operator").val();

        operands.push(operand1);
        operands.push(operand2);
        operators.push(operator);

        var data = {
            "operands": operands,
            "operators": operators
        };

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/api/v1/calculations",
            data: JSON.stringify(data),
            contentType: "application/json",
            success: function(response) {
                $("#result").text(response.result);
            },
            error: function(jqXHR) {
                if (jqXHR.responseJSON && jqXHR.responseJSON.detail) {
                    alert(jqXHR.responseJSON.detail);
                } else {
                    alert("An error occurred during the calculation.");
                }
            }
        });
    });
});
