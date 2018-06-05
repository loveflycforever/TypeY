function manage_reject(mid) {
    $.post("reject", {mid : mid}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}

function manage_approve(mid) {
    $.post("approve", {mid : mid}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}

function manage_collect(mid) {
    $.post("collect", {mid : mid}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}

function manage_publish(mid) {
    $.post("publish", {mid : mid}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}

function manage_remove(mid) {
    $.post("remove", {mid : mid}, function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
        alert(data);
    });
}