Namespace Store

    ''' <summary> A CMake variable. </summary>
    Public Class Variable

#Region "Properties"

        ''' <summary> Gets or sets the variable. </summary>
        ''' <value> The variable. </value>
        Public Property Name As String

        ''' <summary> Gets or sets the value. </summary>
        ''' <value> The value. </value>
        Public Property Value As String

#End Region

#Region "Constructors"

        ''' <summary> Default constructor. </summary>
        Public Sub New()
        End Sub

        ''' <summary> Default Constructor. </summary>
        ''' <param name="name">  The variable. </param>
        ''' <param name="value"> The value. </param>
        Public Sub New(name As String, value As String)
            Me.Name = name
            Me.Value = value
        End Sub

#End Region

#Region "Functions"

        ''' <summary> Return the Cache Entry as a String. </summary>
        ''' <returns> A String that represents this object. </returns>
        Public Overloads Function ToString() As String
            Dim ret As String = Name & " " & Value
            Return ret
        End Function

#End Region

    End Class

End Namespace
