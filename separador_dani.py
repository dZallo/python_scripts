"""
Este script tiene el cometido de tomar un directorio, que puede tener varios niveles de subdirectorios,
hacer una copia con la misma jerarquía, pero sólo manteniendo los archivos de la extensión que
le hayamos indicado

 Ejemplo de comando que ejecuta el script.
    py .separador_dani.py -source a -target b --list ".pdf" "txt"

 Enlaces importantes
 - argparse: Para añadir parametros al comando.
    https://linuxhint.com/add_command_line_arguments_to_a_python_script/

"""
import argparse


def argument_parser():
    """
    Method to add and get the parameters of a command.
    These parsed arguments are also checked by the “argparse” module to ensure that they are of proper “type”.
    The ArgumentParser object is needed to convert command line argument values to data types understood by Python.
    This is done by the “parse_args” method of ArgumentParser object, as shown in the last statement.

    @return: a list of arguments
    """
    parser = argparse.ArgumentParser(
        description="Exercise for copying a directory and the desired files")

    parser.add_argument("-source", "--source_path",
                        help="Path to the directory you want to copy.",
                        type=str, required=True)
    parser.add_argument("-target", "--target_path",
                        help="Path to the directory where you want to make the copy.",
                        type=str, required=True)
    parser.add_argument("-list", "--list_extensions",
                        help='List of file extensions that you want to store and save, the rest is not copied.'
                             'The parameters are passed between quotes ("") e.g.: --list_extensions "eg1" "eg2"...'
                             'If you put "*",all files will be copied.',
                        nargs='*', required=True)
    args = parser.parse_args()
    return args


def check_extension(extensions_to_check: [str]) -> [str]:
    """
    Method to check if the extensions inside of the list, starts with  a ".".
    If the extension doesnt have the "." , the method adds it to the begging
    @param extensions_to_check: a list of strings with or without the dots
    @return list_checked: a list of strings with dots
    """
    list_checked = []

    print("Before")
    print(extensions_to_check)

    for extension in extensions_to_check:
        list_checked.append(extension) if extension.startswith('.') else list_checked.append("." + extension)

    print("After")
    print(list_checked)
    return list_checked


def main():
    print("Innit...")

    # Get the arguments from the script command
    args = argument_parser()
    source_path = args.source_path
    target_path = args.target_path
    extensions_to_save = args.list_extensions

    # Format the arguments to secure the content
    extensions_to_save = check_extension(extensions_to_save)

    # Get the structure of the directories and files from the source_path

    # Generate the structure of the directories and files to target_path

    print("...Finish")


if __name__ == "__main__":
    main()
