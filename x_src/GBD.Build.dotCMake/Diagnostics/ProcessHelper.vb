Imports System.IO

Namespace Diagnostics

    ''' <summary> Base Class for Process Wrappers. </summary>
    Public Class ProcessHelper

#Region "Properties"

        ''' <summary> Underlying System Diagnostics Process. </summary>
        ''' <value> Underlying System Diagnostics Process. </value>
        Public ReadOnly Property Process As Process
            Get
                Return _Process
            End Get
        End Property
        Protected Property _Process As Process

        ''' <summary> Gets or sets the properties to pass to the Start method of the Process. </summary>
        ''' <value> Gets or sets the properties to pass to the Start method of the Process. </value>
        Public Property StartInfo As ProcessStartInfo
            Get
                Return _Startinfo
            End Get
            Set(value As ProcessStartInfo)
                _Startinfo = value
            End Set
        End Property
        Protected Property _Startinfo As ProcessStartInfo

        ''' <summary> Gets the state of the process. </summary>
        ''' <value> Gets the state of the process. </value>
        Public ReadOnly Property State As ProcessState
            Get
                Return _State
            End Get
        End Property
        Protected Property _State As ProcessState

        ''' <summary> Gets or sets the full pathname of the CMake executable file. </summary>
        ''' <value> The full pathname of the CMake executable file. </value>
        Public Property FileName As String
            Get
                Return _Startinfo.FileName
            End Get
            Set(value As String)
                _Startinfo.FileName = value
            End Set
        End Property

        ''' <summary> Gets or sets the pathname of the working directory. </summary>
        ''' <value> The pathname of the working directory. </value>
        Public Property WorkingDirectory As String
            Get
                Return _Startinfo.WorkingDirectory
            End Get
            Set(value As String)
                _Startinfo.WorkingDirectory = value
            End Set
        End Property

        ''' <summary> Command Line Options to pass to the process. </summary>
        ''' <value> The process options. </value>
        Public Property Arguments As String
            Get
                Return _Startinfo.Arguments
            End Get
            Set(value As String)
                _Startinfo.Arguments = value
            End Set
        End Property

#End Region

#Region "Types"

        ''' <summary> Represents the current state of the process. </summary>
        Public Enum ProcessState
            Stopped = 0
            Started = 1
        End Enum

#End Region

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
            _Startinfo = New ProcessStartInfo
        End Sub

        ''' <summary> Default Constructor. </summary>
        ''' <param name="exepath"> The full pathname of the CMake executable file. </param>
        Public Sub New(exepath As String)
            Me.New()
            FileName = exepath
        End Sub

        ''' <summary> Constructor. </summary>
        ''' <param name="exepath"> The full pathname of the CMake executable file. </param>
        ''' <param name="args">    Command Line Arguments for the exe. </param>
        Public Sub New(exepath As String, args As String)
            Me.New()
            FileName = exepath
            Arguments = args
        End Sub

        ''' <summary>
        ''' Allows an object to try to free resources and perform other cleanup operations before it is
        ''' reclaimed by garbage collection.
        ''' </summary>
        Protected Overrides Sub Finalize()
            Close()
            MyBase.Finalize()
        End Sub

#End Region

#Region "Functions - Start / Stop"

        ''' <summary> Launches CMake. </summary>
        ''' <param name="args"> Command Line Arguments for the exe. </param>
        Public Sub Launch(args As String)
            Arguments = args
            Launch()
        End Sub

        ''' <summary> Launches CMake. </summary>
        Public Sub Launch()
            Try
                _Process = New Process
                AddHandler _Process.Exited, AddressOf ExitHandler
                _Process.StartInfo = _Startinfo
                _Startinfo.RedirectStandardOutput = True
                _Startinfo.RedirectStandardError = True
                _Startinfo.RedirectStandardInput = True
                _Startinfo.UseShellExecute = False
                ' The command line is supressed to keep the process in the background
                _Startinfo.CreateNoWindow = True
                _Startinfo.WindowStyle = ProcessWindowStyle.Hidden
                _Process.Start()
                _State = ProcessState.Started
            Catch ex As Exception
                Throw New Exception("An error occurred running " & FileName & ".", ex)
            End Try
        End Sub

        ''' <summary> Wait for process to Exit. </summary>
        Public Sub WaitForExit()
            If _Process IsNot Nothing Then _Process.WaitForExit()
        End Sub

        ''' <summary> Wait for process to Exit. </summary>
        Public Function WaitForExit(milliseconds As Integer) As Boolean
            If _Process IsNot Nothing Then Return _Process.WaitForExit(milliseconds)
            Return False
        End Function

        ''' <summary> Closes this process. </summary>
        Public Sub Close()
            _State = ProcessState.Stopped
            If _Process IsNot Nothing Then _Process.Close()
        End Sub

#End Region

#Region "Functions - Read / Write"

        ''' <summary> Reads standard out. </summary>
        ''' <returns> The standard out. </returns>
        Public Function ReadStdOut() As String
            If _Process Is Nothing Then Return ""
            Dim tmpstr As StreamReader = _Process.StandardOutput
            Dim ret As String = tmpstr.ReadToEnd
            tmpstr.Close()
            Return ret
        End Function

        ''' <summary> Reads standard error. </summary>
        ''' <returns> The standard error. </returns>
        Public Function ReadStdErr() As String
            If _Process Is Nothing Then Return ""
            Dim tmpstr As StreamReader = _Process.StandardError
            Dim ret As String = tmpstr.ReadToEnd
            tmpstr.Close()
            Return ret
        End Function

        ''' <summary> Writes to Standard Input. </summary>
        ''' <param name="input"> The input to write. </param>
        Public Sub WriteStdIn(input As String)
            If _Process Is Nothing Then Throw New Exception("Process is not Open")
            Dim tmpstr As StreamWriter = _Process.StandardInput
            tmpstr.Write(input)
            tmpstr.Close()
        End Sub

#End Region

#Region "Functions - Handlers"

        ''' <summary> Handler, called when the process exits. </summary>
        ''' <param name="sender"> Source of the event. </param>
        ''' <param name="e">      Event information. </param>
        Protected Sub ExitHandler(sender As Object, e As EventArgs)
            ' Doesn't seem to work for some reason
            _State = ProcessState.Stopped
        End Sub

#End Region

    End Class

End Namespace
