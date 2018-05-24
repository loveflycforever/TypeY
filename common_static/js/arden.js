function manage_approve() {
    $.post("approve", {}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}

function manage_reject() {
    $.post("reject", {}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}