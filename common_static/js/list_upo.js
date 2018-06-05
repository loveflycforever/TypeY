function listAll(mid) {
    $.get("listUpo", function (resp) {
        var status = resp.status;
        var message = resp.message;
        var data = resp.data;
    });
}
