
' Command Line Options to pass to CMake
' http://www.cmake.org/cmake/help/v3.2/manual/cmake.1.html

' TODO List Toolset names? / Platform Names?

Imports GBD.Build.dotCMake.Store

Namespace Diagnostics.CMake

    Public Class BuildLauncher
        Inherits BaseLauncher

#Region "Properties"

        ''' <summary> Pre-load a script to populate the cache. </summary>
        ''' <value> The path to the cache file to load. </value>
        Public Property LoadCacheFile As String

        ''' <summary> Override Cache Entries within CMake Cache. </summary>
        ''' <value> The cache entries to override. </value>
        Public Property CacheVariables As List(Of CacheVariable)

        ''' <summary> Remove Entries from the CMake Cache using globbing pattern. </summary>
        ''' <value> The globbing patterns to remove. </value>
        Public Property CacheRemoveEntries As List(Of String)

        ''' <summary> Select the Generator to use, to generate the project files. </summary>
        ''' <value> The generator to use, e.g. makefiles / Visual Studio files etc. </value>
        Public Property BuildSystemGenerator As String

        ''' <summary> Specify toolset name if supported by generator. </summary>
        ''' <value> The name of the tool set. </value>
        Public Property ToolSetName As String

        ''' <summary> Specify platform name if supported by generator. </summary>
        ''' <value> The name of the platform to use. </value>
        Public Property PlatformName As String

#End Region

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

        ' TODO Move to Info

        ''' <summary> Gets the available Generators for the current platform. </summary>
        ''' <returns> The available Generators for the current platform. </returns>
        Public Function GetGenerators() As List(Of String)
            Dim ret As New List(Of String)

            ' TODO run cmake --help then parse the output

            Return ret
        End Function

        ''' <summary> Convert this list of options into a string that can be passed to a CMake Process. </summary>
        Public Sub Populate_CmdOptions()
            _CommandLineOpts.Clear()

            ' CMake -C Options
            If Not String.IsNullOrEmpty(LoadCacheFile) Then _CommandLineOpts.Add("LoadCacheFile", "-C " & LoadCacheFile)
            ' CMake -D Options
            If CacheVariables IsNot Nothing Then
                For Each item In CacheVariables
                    _CommandLineOpts.Add("CacheVariable_" & item.ToString, "-D """ & item.ToString & """")
                Next
            End If
            ' CMake -U Options
            If CacheRemoveEntries IsNot Nothing Then
                For Each item In CacheRemoveEntries
                    _CommandLineOpts.Add("CacheRemoveEntry_" & item.ToString, "-U """ & item & """")
                Next
            End If
            ' CMake -G Options
            If Not String.IsNullOrEmpty(BuildSystemGenerator) Then _CommandLineOpts.Add("BuildSystemGenerator", "-G """ & BuildSystemGenerator & """")
            ' CMake -T Options
            If Not String.IsNullOrEmpty(ToolSetName) Then _CommandLineOpts.Add("ToolSetName", "-T """ & ToolSetName & """")
            ' CMake -A Options
            If Not String.IsNullOrEmpty(PlatformName) Then _CommandLineOpts.Add("PlatformName", "-A """ & PlatformName & """")

        End Sub

#End Region

    End Class

End Namespace
