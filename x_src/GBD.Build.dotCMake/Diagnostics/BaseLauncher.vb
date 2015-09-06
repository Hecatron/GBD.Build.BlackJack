Imports System.Text

Namespace Diagnostics

    ''' <summary> Base Class for Options. </summary>
    Public Class BaseLauncher

#Region "Properties"

        ''' <summary> Gets the CMake process. </summary>
        ''' <value> The CMake process. </value>
        Public ReadOnly Property ProcessHelper As ProcessHelper
            Get
                Return _ProcessHelper
            End Get
        End Property
        Protected Property _ProcessHelper As ProcessHelper

        ''' <summary> Options for the Command Line. </summary>
        ''' <value> Options for the Command Line. </value>
        Public ReadOnly Property CommandLineOpts As Dictionary(Of String, String)
            Get
                Return _CommandLineOpts
            End Get
        End Property
        Protected Property _CommandLineOpts As Dictionary(Of String, String)

        ''' <summary> Standard Output from the Process. </summary>
        ''' <value> The standard output. </value>
        Public ReadOnly Property StdOut As String
            Get
                Return _StdOut
            End Get
        End Property
        Protected Property _StdOut As String

        ''' <summary> The Standard Error Output from the Process. </summary>
        ''' <value> The standard error. </value>
        Public ReadOnly Property StdErr As String
            Get
                Return _StdErr
            End Get
        End Property
        Protected Property _StdErr As String

#End Region

#Region "Constructors"

        ''' <summary> Default Constructor. </summary>
        Public Sub New()
            _CommandLineOpts = New Dictionary(Of String, String)
        End Sub

        ''' <summary> Default Constructor. </summary>
        ''' <param name="proc"> The CMakeProcess. </param>
        Public Sub New(proc As ProcessHelper)
            _CommandLineOpts = New Dictionary(Of String, String)
            _ProcessHelper = proc
        End Sub

#End Region

#Region "Functions"

        ''' <summary> Convert this object into a string representation. </summary>
        ''' <returns> A String that represents this object. </returns>
        Public Overloads Function ToString() As String
            Return GetCommandLine()
        End Function

        ''' <summary> Gets the command line options as a string. </summary>
        ''' <returns> The command line options as a string. </returns>
        Public Function GetCommandLine() As String
            Dim ret As New StringBuilder
            For Each item In _CommandLineOpts
                ret.Append(item.Value & " ")
            Next
            Return ret.ToString
        End Function

        ''' <summary> Executes the CMake Process and return Standard Out / . </summary>
        Public Sub Launch()
            _ProcessHelper.Launch(GetCommandLine())
            _StdOut = _ProcessHelper.ReadStdOut
            _StdErr = _ProcessHelper.ReadStdErr
            _ProcessHelper.WaitForExit()
            _ProcessHelper.Close()
        End Sub

#End Region

    End Class

End Namespace
