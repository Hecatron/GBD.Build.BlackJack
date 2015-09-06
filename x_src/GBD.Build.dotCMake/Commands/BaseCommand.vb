
' Base Class for all CMake Commands.
' http://www.cmake.org/cmake/help/v3.2/manual/cmake-language.7.html

Imports System.Text

Namespace Commands

    ''' <summary> Base Class for all CMake Commands. </summary>
    Public Class BaseCommand

#Region "Properties"

        ''' <summary> Gets the name of the command. </summary>
        ''' <value> The name of the command. </value>
        Public ReadOnly Property CommandName As String
            Get
                Return _CommandName
            End Get
        End Property
        Protected Property _CommandName As String

        ''' <summary> List of Arguments to pass to the Command. </summary>
        ''' <value> List of Arguments to pass to the Command. </value>
        Public Overridable ReadOnly Property Arguments As List(Of String)
            Get
                Return _Arguments
            End Get
        End Property
        Protected Property _Arguments As List(Of String)

#End Region

#Region "Constructors"

        ''' <summary> Default Constructor. </summary>
        ''' <param name="commandname"> The name of the command. </param>
        Public Sub New(commandname As String)
            _CommandName = commandname
            _Arguments = New List(Of String)
        End Sub

        ''' <summary> Constructor. </summary>
        ''' <param name="commandname"> The name of the command. </param>
        ''' <param name="args">        The arguments. </param>
        Public Sub New(commandname As String, args As List(Of String))
            _CommandName = commandname
            _Arguments = args
        End Sub

#End Region

#Region "Functions"

        ''' <summary> Converts this object to a CMake String Command. </summary>
        ''' <returns> This object as a String Command. </returns>
        Public Overridable Function ToCommand() As String
            Dim ret As New StringBuilder
            ret.Append(" " & CommandName & " (")
            For Each item In Arguments
                ret.Append(item)
            Next
            ret.Append(" ) ")
            Return ret.ToString
        End Function

        ''' <summary> Convert this object into a string representation. </summary>
        ''' <returns> A String that represents this object. </returns>
        Public Overridable Overloads Function ToString() As String
            Return ToCommand()
        End Function

#End Region

    End Class

End Namespace
