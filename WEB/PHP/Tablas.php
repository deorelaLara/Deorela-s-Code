<head>
	<meta charset="UTF-8">
	<title>Tables</title>
</head>
<body>
    <form action="ok" method="POST">
        <label for="num"><h2>Introduce los siguientes datos </h2></label><br>
       
        <label>¿Que tabla de multiplicar deseas?</label>
        <input type="text" name="numTabla" required><br>
       
        <label>Limite de tu tabla: </label>
        <input type="text" name="rango" required>
        
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
<style>
    h2{
        color: blue;
    }
</style>

<?php
    if($_POST){
        echo "Hola";
    }
?>
<!--<script>
    var numTabla = parseInt(window.prompt("¿Que tabla quieres?"));
    var rango = parseInt(window.prompt("Limite de la tabla: "))
    document.write("<h2> Tabla de multiplicar del " + numTabla + "</h2>")
    document.write("<ul>");
    for(x = 1; x <= rango; x++){
        document.write("<li>");
        document.write(numTabla + "x" + x + "=" + numTabla * x);
        document.write("</li>")
    }
    document.write("</ul>");
</script> -->
