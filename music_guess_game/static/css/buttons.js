<script>
    // Replace the button text with the answers
    {% for answer in answers %}
    document.querySelector("#button-{{ loop.index }}").textContent = "{{ answer[0] }} - {{ answer[2] }}";
    {% endfor %}

    // Disable the buttons when one of them is clicked
    document.querySelectorAll(".btn").forEach(function(button) {
        button.addEventListener("click", function() {
            document.querySelectorAll(".btn").forEach(function(btn) {
                btn.setAttribute("disabled", true);
            });
        });
    });
</script>


<script
>
    $(document).ready(function(){
        $(".btn").click(function(){
            if ($(this).html() == 'yes') {
                $(this).removeClass("btn-outline-primary").addClass("btn-success");
            }
            else {
                $(this).removeClass("btn-outline-primary").addClass("btn-danger");
            }
            $(this).attr('disabled','disabled');
        });
    });
</script>