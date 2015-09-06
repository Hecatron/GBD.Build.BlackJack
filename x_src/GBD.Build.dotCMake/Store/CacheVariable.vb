
Namespace Store

    ''' <summary> A CMake cache variable. </summary>
    Public Class CacheVariable
        Inherits Variable

#Region "Properties"

        ''' <summary> Gets or sets the type of the variable. </summary>
        ''' <value> The type of the variable. </value>
        Public Property VariableType As VarType

        ''' <summary> Gets or sets the document string. </summary>
        ''' <value> The document string. </value>
        Public Property DocString As String

#End Region

#Region "Types"

        ''' <summary> Type of Cache Variable. </summary>
        Public Enum VarType
            VarFilePath
            VarPath
            VarString
            VarBool
            Internal
        End Enum


#End Region

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
        End Sub

        ''' <summary> Default Constructor. </summary>
        ''' <param name="var">     The variable. </param>
        ''' <param name="vartype"> The type of the variable. </param>
        ''' <param name="value">   The value. </param>
        Public Sub New(var As String, vartype As VarType, value As String)
            Name = var
            VariableType = vartype
            Me.Value = value
        End Sub

#End Region

#Region "Functions"

        ''' <summary> Return the Cache Entry as a String. </summary>
        ''' <returns> A String that represents this object. </returns>
        Public Overloads Function ToString() As String
            Dim ret As String = Name & ":" & VariableType.ToString & "=" & Value
            Return ret
        End Function

#End Region

    End Class

End Namespace
