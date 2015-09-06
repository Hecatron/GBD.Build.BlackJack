Imports System.IO

Namespace Commands

    ''' <summary> link directories command. </summary>
    Public Class link_directories
        Inherits BaseCommand

#Region "Properties"

        ''' <summary> Gets or sets a list of directories. </summary>
        ''' <value> A List of directories. </value>
        Public Property DirectoryList As List(Of String)

#End Region

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
            MyBase.New("link_directories")
            DirectoryList = Arguments
        End Sub

        ''' <summary> Constructor. </summary>
        ''' <param name="directorylist"> A List of directories. </param>
        Public Sub New(directorylist As List(Of String))
            MyBase.New("link_directories")
            _Arguments = directorylist
            Me.DirectoryList = Arguments
        End Sub

#End Region

#Region "Functions"

        ''' <summary> Converts this object to a CMake String Command. </summary>
        ''' <returns> This object as a String Command. </returns>
        Public Overrides Function ToCommand() As String
            ' Check the paths exist
            For Each item In DirectoryList
                If Directory.Exists(item) = False Then Throw New DirectoryNotFoundException("Link Directory Not Found: " & item)
            Next
            Return MyBase.ToCommand
        End Function

#End Region

    End Class

End Namespace
