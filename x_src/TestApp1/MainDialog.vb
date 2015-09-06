
Imports GBD.Build.dotCMake.Diagnostics.CMake

Public Class MainDialog

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim launcher1 As New InfoLauncher
        launcher1.Manual_Variables()
        StdOutTxt.Text = launcher1.StdOut
        StdErrTxt.Text = launcher1.StdErr
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click


    End Sub
End Class
