Namespace Commands

    ''' <summary> Output a Message via CMake. </summary>
    Public Class message
        Inherits BaseCommand

#Region "Properties"

        ''' <summary> The message to output via CMake. </summary>
        ''' <value> The message to output via CMake. </value>
        Public Property Message As String

        ''' <summary> List of Arguments to pass to the Command. </summary>
        ''' <value> List of Arguments to pass to the Command. </value>
        Public Overrides ReadOnly Property Arguments As List(Of String)
            Get
                Dim ret As New List(Of String)
                ret.Add(Message)
                Return ret
            End Get
        End Property

#End Region

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
            MyBase.New("message")
            Message = ""
        End Sub

        ''' <summary> Constructor. </summary>
        ''' <param name="message"> A Message to output. </param>
        Public Sub New(message As String)
            MyBase.New("message")
            Me.Message = message
        End Sub

#End Region

    End Class

End Namespace
