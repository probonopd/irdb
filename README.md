# irdb

![ir](https://cloud.githubusercontent.com/assets/2480569/9023330/cc63e7fe-3897-11e5-94cb-8cb145971fd2.png)

One of the largest crowd-sourced, manufacturer-independent databases of infrared remote control codes on the web, and aspiring to become the most comprehensive and most accurate one. Think of it as the "Wikipedia of infrared remote control codes".

## Usage

This database contains infrared remote control codes in a very space-efficient way, using protocol, device, subdevice, function notation. Using this information, you can render signals to raw timings, Pronto Hex, or other formats using software like [IrScrutinizer](https://github.com/bengtmartensson/harctoolboxbundle) or [MakeHex](https://github.com/probonopd/MakeHex).

## Accessing

If you would like to access this database from your product (e.g., app) it is suggested that you do not bundle the database as a whole but access it dynamically at runtime. By doing so, your product will benefit from updates of the database automatically.

To access the database with any amount of traffic, it is recommended to use the [RawGit](https://rawgit.com) content delivery network (CDN).

For example, instead of accessing files from GitHub locally, you should access them over [RawGit](https://rawgit.com) like this:

```
http://cdn.rawgit.com/probonopd/irdb/master/codes/index
http://cdn.rawgit.com/probonopd/irdb/master/codes/Samsung/TV/7,7.csv
```

## Contributing

1. Check whether the code you want to contribute is already in the database
2. If it is not, click the "edit" button to change/edit a file
3. Follow the naming conventions for files, `<manufacturer>/<devicetype>/<device>,<subdevice>.csv`
4. Make sure the file contains the codes in ascending order of commands
5. Create a pull request and state the device you have used to create the file in the comment

## Examples

In this section, projects and products will be listed which include or access irdb.
* [irdb.tk](http://irdb.tk) website that allows you to search the database and render codes in various formats
* [IrScrutinizer](https://github.com/bengtmartensson/harctoolboxbundle) software that can import infrared remote signals from irdb, scrutinize them, and send them using various sending devices

## License

You may include or access this database from your product (e.g., app) provided that you follow the terms of the [irdb License](https://github.com/probonopd/irdb/blob/master/LICENSE.md).
