{% block imports %}
from blackjack.cmake.ScriptBase import ScriptBase
{% endblock %}


{% block Func_ClassDeclr %}
class {{ CmdName }}(ScriptBase):

    """
    CMake Command - {{ CmdName }}
    """
{% endblock %}


{% block Func_ClassInit %}
    def __init__(self
{% for arg in args %}
    ,{{ arg.name }}: {{ arg.type }}
{% endfor %}
):
        super().__init__()
{% for arg in args %}
        self.{{ arg.name }} = {{ arg.name }}
        """{{ arg.description }}"""
{% endfor %}
        return
{% endblock %}


{% block Func_CommandName %}
    @property
    def CommandName(self):
        """Name of the command"""
        return {{ CmdName }}
{% endblock %}


{% block Func_Render %}
	def render_body(self):
        ret = []
        {{ Render_Code }}
		return ret
{% endblock %}
