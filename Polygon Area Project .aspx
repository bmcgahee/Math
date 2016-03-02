//aspx code for PolygonArea project

<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="PolygonArea.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Area of a Polygon</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <h1><em>Area of a Polygon</em></h1>
        <p><strong>Number of sides =</strong>&nbsp;
            <asp:TextBox ID="sidesTextBox" runat="server"></asp:TextBox>
&nbsp;
            <asp:Label ID="Label1" runat="server" Text="Enter an integer greater than 2 for the number of sides."></asp:Label>
            <br />
            <strong>Radius =</strong>&nbsp;
            <asp:TextBox ID="radiusTextBox" runat="server"></asp:TextBox>
&nbsp;&nbsp;
            <asp:Label ID="Label2" runat="server" Text="Enter a positive integer for the radius. "></asp:Label>
        </p>
        <p>
            <asp:Button ID="getAreaButton" runat="server" OnClick="getAreaButton_Click" Text="Get Area" />
        </p>
        <p>The Area is:&nbsp; <asp:Label ID="areaLabel" runat="server"></asp:Label>
        </p>
    </div>
    </form>
</body>
</html>
