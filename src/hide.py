from IPython.display import HTML

class Hide:
    def hide():
        return HTML('''<script>
        code_show=true; 
        function code_toggle() {
        if (code_show){
        $('div.input').hide();
        } else {
        $('div.input').show();
        }
        code_show = !code_show
        } 
        $( document ).ready(code_toggle);
        </script>
        Click <a href="javascript:code_toggle()">here</a> to enable code.''')