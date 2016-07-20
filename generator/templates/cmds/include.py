{% extends "cmd_base_tmpl.py" %}

{% set args = [
('FilePath', 'str', 'File path to import, or the name of the cmake module to import', ''),
('Optional', 'bool', 'If Optional is set, then no error is raised if the file does not exist.', 'False'),
('ResultVar', 'str', '', 'None'),
('NoPolicyScope', 'str', '', 'False'),
] %}

{% block Func_Render_Body_Inner %}
        filepath = self.FilePath
        if isinstance(filepath, BaseModule):
            filepath = filepath.get_modulename()
        tmpline = "{{ CmdName }}(" + filepath + " "
        if self.Optional:
            tmpline += "OPTIONAL "
        if self.ResultVar:
            tmpline += "RESULT_VARIABLE " + self.ResultVar
        if self.NoPolicyScope:
            tmpline += "NO_POLICY_SCOPE "
        tmpline += ")"
        ret = [tmpline]
{% endblock %}
