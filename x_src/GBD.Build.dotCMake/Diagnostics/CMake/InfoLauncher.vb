
' TODO policies next

Namespace Diagnostics.CMake

    ''' <summary> Launcher for Help / Documentation Output. </summary>
    Public Class InfoLauncher
        Inherits BaseLauncher

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
            MyBase.New()
            _ProcessHelper = New ProcessHelper("cmake")
        End Sub

        ''' <summary> Default Constructor. </summary>
        ''' <param name="proc"> The CMakeProcess. </param>
        Public Sub New(proc As ProcessHelper)
            MyBase.New(proc)
        End Sub

#End Region

#Region "Functions"

        Public Function Help_Useage() As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help")
            Launch()

            ' TODO
            Return ""
        End Function

#End Region

#Region "Functions - Variables Info"

        ''' <summary> List properties with help available and exit. </summary>
        ''' <returns> Properties List. </returns>
        Public Function Properties_List() As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-property-list ")
            Launch()

            ' TODO
            Return ""
        End Function

        ''' <summary> Return Help Information for a given Property. </summary>
        ''' <param name="prop"> The property. </param>
        ''' <returns> A String representing the help info. </returns>
        Public Function Properties_HelpInfo(prop As String) As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-property " & prop)
            Launch()

            ' TODO
            Return ""
        End Function

        ''' <summary> List variables with help available and exit. </summary>
        ''' <returns> Variables List. </returns>
        Public Function Variable_List() As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-variable-list")
            Launch()

            ' TODO
            Return ""
        End Function

        ''' <summary> Return Help Information for a given Variable. </summary>
        ''' <param name="var"> The variable to lookup. </param>
        ''' <returns> A String representing the help info. </returns>
        Public Function Variable_HelpInfo(var As String) As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-variable " & var)
            Launch()

            ' TODO
            Return ""
        End Function

#End Region

#Region "Functions - Manual Info"

        ''' <summary> Print cmake-properties manual and exit. </summary>
        ''' <returns> cmake-properties manual. </returns>
        Public Function Manual_Properties() As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-properties")
            Launch()

            ' TODO
            Return ""
        End Function

        ''' <summary> Print cmake-variables manual and exit. </summary>
        ''' <returns> cmake-variables manual. </returns>
        Public Function Manual_Variables() As String
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("Help", "--help-variables")
            Launch()
            If Not String.IsNullOrEmpty(StdErr) Then Throw New Exception("Error Processing Command" & vbCrLf & StdErr)
            Return _StdOut
        End Function

#End Region

    End Class

End Namespace
