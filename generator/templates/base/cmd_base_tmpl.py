{%- block imports -%}
from blackjack.cmake.ScriptBase import ScriptBase
{%- endblock %}

{% block Func_ClassDeclr -%}
class {{ CmdName }}(ScriptBase):

    """
    CMake Command - {{ CmdName }}
    """
{%- endblock %}

{% block Func_ClassInit %}
    def __init__(self
{%- for argname, argtype, argdesc, argdef in args -%}
, {{ argname|lower }}: {{ argtype }} {% if argdef -%} = {{ argdef }} {%- endif %}
{%- endfor -%}
):
        super().__init__()
{%- for argname, argtype, argdesc, argdef in args %}
        self.{{ argname }} = {{ argname|lower }}
        {%- if argdesc %}
        """{{ argdesc }}"""
        {%- endif -%}
{%- endfor %}
        return
{%- endblock %}

{% block Func_CommandName %}
    @property
    def CommandName(self):
        """Name of the command"""
        return "{{ CmdName }}"
{%- endblock %}

{% block Func_Render_Body %}
	def render_body(self):
        ret = []
        {%- block Func_Render_Body_Inner %}{% endblock %}
		return ret
{%- endblock %}
