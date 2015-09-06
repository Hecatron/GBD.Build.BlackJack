Namespace Diagnostics.CMake

    ''' <summary> A Command Line Tools Launcher. </summary>
    Public Class CLTLauncher
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

        ''' <summary> Compare files. </summary>
        ''' <param name="file1"> The first file. </param>
        ''' <param name="file2"> The second file. </param>
        ''' <returns> true if it succeeds, false if it fails. </returns>
        Public Function CompareFiles(file1 As String, file2 As String) As Boolean
            _CommandLineOpts.Clear()
            _CommandLineOpts.Add("CLT", "-E compare_files")
            _CommandLineOpts.Add("file1", file1)
            _CommandLineOpts.Add("file2", file2)
            Launch()

            ' TODO parse output

            Return False
        End Function

        ' TODO

#End Region

    End Class

End Namespace
